from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm


# Create your views here.
def user_profile(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserForm()
    return render(request, 'user_profile.html', {'form': form})

def matching_view(request):
    player = User.objects.last()  # 最新のユーザーを取得
    opponents = User.objects.exclude(id=player.id)  # 他のユーザーを取得

    each_count_requirements = []
    each_count_personalities = []
    each_count_hobbies = []
    each_count_all = []

    for opponent in opponents:
        count_a = 0
        count_b = 0
        count_c = 0

        if player.purpose == opponent.purpose:
            count_a += 1
        if player.opp_gender == opponent.gender and player.opp_age <= opponent.age <= player.opp_age + 10:
            count_a += 1
        each_count_requirements.append(count_a)

        if player.personality_1 == opponent.personality_1:
            count_b += 1
        if player.personality_2 == opponent.personality_2:
            count_b += 1
        each_count_personalities.append(count_b)

        if player.hobby_1 == opponent.hobby_1:
            count_c += 1
        if player.hobby_2 == opponent.hobby_2:
            count_c += 1
        each_count_hobbies.append(count_c)

        each_count_all.append(count_a + count_b + count_c)

    sorted_indices = sorted(range(len(each_count_all)), key=lambda i: each_count_all[i], reverse=True)
    top_matches = [opponents[i] for i in sorted_indices[:3]]

    return render(request, 'matching_results.html', {'top_matches': top_matches})