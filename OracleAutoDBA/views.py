from django.shortcuts import render, redirect
from django.contrib import messages
from .models import OracleInstance
from .utils import perform_db_tasks, connect_to_oracle, get_instance_details

def index(request):
    if request.method == 'POST':
        # Save instance details
        instance = OracleInstance(
            name=request.POST['name'],
            dsn=request.POST['dsn'],
            username=request.POST['username'],
            password=request.POST['password']
        )
        instance.save()

        # Attempt to connect to the Oracle instance
        try:
            connection = connect_to_oracle(instance)
            if connection:
                # Connection successful, fetch important details
                instance_details = get_instance_details(connection)
                request.session['instance_details'] = instance_details
                messages.success(request, 'Successfully connected to the Oracle instance!')
                return redirect('dashboard')
        except Exception as e:
            messages.error(request, f'Error connecting to Oracle instance: {e}')
            return redirect('index')

    return render(request, 'OracleAutoDBA/index.html')

from django.shortcuts import render
from .models import OracleInstance
from .utils import get_tablespace_usage, get_active_sessions, get_dba_users

from django.shortcuts import render, redirect
from .models import OracleInstance
from .utils import get_performance_metrics

def dashboard(request):
    instance = OracleInstance.objects.last()
    metrics = {}

    if instance:
        metrics = get_performance_metrics(instance)

    return render(request, 'OracleAutoDBA/dashboard.html', {'instance': instance, 'metrics': metrics})


def tablespace_usage(request):
    instance = OracleInstance.objects.latest('id') if OracleInstance.objects.exists() else None
    if instance:
        usage = get_tablespace_usage(instance)
        return render(request, 'OracleAutoDBA/tablespace_usage.html', {'usage': usage})
    return redirect('index')

def active_sessions(request):
    instance = OracleInstance.objects.latest('id') if OracleInstance.objects.exists() else None
    if instance:
        sessions = get_active_sessions(instance)
        return render(request, 'OracleAutoDBA/active_sessions.html', {'sessions': sessions})
    return redirect('index')

def dba_users(request):
    instance = OracleInstance.objects.latest('id') if OracleInstance.objects.exists() else None
    if instance:
        users = get_dba_users(instance)
        return render(request, 'OracleAutoDBA/dba_users.html', {'users': users})
    return redirect('index')


def run_tasks(request):
    # This function can be used for additional tasks if needed
    return render(request, 'OracleAutoDBA/run_tasks.html')
