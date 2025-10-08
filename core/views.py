from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
from .models import ColorfulHairCount

@login_required
def home(request):
        user_counts = ColorfulHairCount.objects.filter(user=request.user)
        total_count_obj = user_counts.aggregate(Sum('value'))
        total_count = total_count_obj['value__sum'] if total_count_obj['value__sum'] is not None else 0

        context = {
            'total_count': total_count,
        }
        return render(request, 'core/home.html', context)

@login_required
def increment_count(request):
        if request.method == 'POST':
            ColorfulHairCount.objects.create(user=request.user, value=1)
        return redirect('home')

@login_required
def decrement_count(request):
        if request.method == 'POST':
            # Можно добавить логику, чтобы не уходить в минус, если это нежелательно
            user_counts = ColorfulHairCount.objects.filter(user=request.user)
            total_count_obj = user_counts.aggregate(Sum('value'))
            current_total = total_count_obj['value__sum'] if total_count_obj['value__sum'] is not None else 0

            if current_total > 0: # Только если текущий счетчик больше нуля
                ColorfulHairCount.objects.create(user=request.user, value=-1)
        return redirect('home')

@login_required
def statistics(request):
        user_counts = ColorfulHairCount.objects.filter(user=request.user)

        # Общая статистика
        total_count_obj = user_counts.aggregate(Sum('value'))
        total_count = total_count_obj['value__sum'] if total_count_obj['value__sum'] is not None else 0

        # Статистика за день
        today = timezone.now().date()
        daily_count_obj = user_counts.filter(timestamp__date=today).aggregate(Sum('value'))
        daily_count = daily_count_obj['value__sum'] if daily_count_obj['value__sum'] is not None else 0

        # Статистика за неделю (последние 7 дней)
        one_week_ago = timezone.now() - timedelta(days=7)
        weekly_count_obj = user_counts.filter(timestamp__gte=one_week_ago).aggregate(Sum('value'))
        weekly_count = weekly_count_obj['value__sum'] if weekly_count_obj['value__sum'] is not None else 0

        # Статистика за месяц (последние 30 дней)
        one_month_ago = timezone.now() - timedelta(days=30)
        monthly_count_obj = user_counts.filter(timestamp__gte=one_month_ago).aggregate(Sum('value'))
        monthly_count = monthly_count_obj['value__sum'] if monthly_count_obj['value__sum'] is not None else 0

        # Детальная статистика по дням
        daily_breakdown = user_counts.values('timestamp__date').annotate(
            day_total=Sum('value')
        ).order_by('-timestamp__date')[:7] # Последние 7 дней

        context = {
            'total_count': total_count,
            'daily_count': daily_count,
            'weekly_count': weekly_count,
            'monthly_count': monthly_count,
            'daily_breakdown': daily_breakdown,
        }
        return render(request, 'core/statistics.html', context)
