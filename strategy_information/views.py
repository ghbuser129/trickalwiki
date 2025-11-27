from django.shortcuts import render, redirect, get_object_or_404
from .models import Strategy, Comment
from .forms import StrategyForm, CommentForm, ContactForm
from django.core.mail import EmailMessage
from django.conf import settings

# トップページ（攻略情報一覧）
def index(request):
    strategies = Strategy.objects.all()
    return render(request, "index.html", {"strategies": strategies})

# 攻略情報登録ページ
def add_strategy(request):
    if request.method == "POST":
        form = StrategyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")  # 登録後は一覧へ戻る
    else:
        form = StrategyForm()
    return render(request, "add_strategy.html", {"form": form})

# 攻略情報詳細ページ（コメント掲示板付き）
def strategy_detail(request, pk):
    strategy = get_object_or_404(Strategy, pk=pk)
    comments = strategy.comments.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.strategy = strategy
            comment.save()
            return redirect("strategy_detail", pk=pk)
    else:
        form = CommentForm()
    return render(
        request,
        "detail.html",
        {"strategy": strategy, "comments": comments, "form": form}
    )

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "お問い合わせが届きました"
            body = f"""
            名前: {form.cleaned_data['name']}
            メール: {form.cleaned_data['email']}
            内容:
            {form.cleaned_data['message']}
            """

            # EmailMessage をここで使う
            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.DEFAULT_FROM_EMAIL,  # 送信元（英数字のメールアドレス）
                to=["aiueo1295656@gmail.com"],  # 受信先
            )
            email.content_subtype = "plain"   # テキストメール
            email.encoding = "utf-8"          # ←ここでUTF-8指定
            email.send()

            return redirect("index")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})

