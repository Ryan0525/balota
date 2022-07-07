from django.shortcuts import render, redirect
from django.http import HttpResponse
from msystem.models import Member_info, Program, Branch, Barangay_report, Member_report
from django.views.decorators.csrf import csrf_exempt
#from msystem import settings


def home_page(request):
    MemberInfo = Member_info.objects.all()
    return render(request, 'homepage.html', {'MemberInfo':MemberInfo})

def ca_sh(request, AssistanceId):
    Assistance = Member_info.objects.get(id=AssistanceId)
    assist = Program.objects.filter(member_info=AssistanceId)
    branch = Branch.objects.get(member_branch=AssistanceId)
    return render(request, 'assistance.html', {'member_info': Assistance, 'assist': assist, 'branch': branch})

def cas_h(request, AssistanceId):
    Assistance = Member_info.objects.get(id=AssistanceId)
    Program.objects.create(Rate=request.POST['rate'],Days=request.POST['days'], Months=request.POST['deduct'],Total=request.POST['total'],Date_time=request.POST['salarydate'], member_info=Assistance)
    return redirect(f'/4ps/cash/{Assistance.id}/')

def ass_list(request):
    MemberInfo = Member_info.objects.all()
    return render(request, 'Financial.html', {'member_info':MemberInfo})

def n_member(request):
    newInfo = Member_info.objects.create(Name=request.POST['name'], Age=request.POST['age'], Brgy=request.POST['brgy'], Contact_No=request.POST['contact_num'], ZipCode=request.POST['address'], DSWD_id=request.POST['comid'],Gender=request.POST['gender'])
    return redirect(f'/msystem/branch/{newInfo.id}/')     


def member_p(request):
    return render(request, 'Memberinfo.html')

def mem_list(request):
    MemberInfo = Member_info.objects.all()
    return render(request, 'mem_list.html', {'member_info':MemberInfo})


def branch_br(request, BranchId):
    MemBranch = Member_info.objects.get(id=BranchId)
  
    return render(request, 'BranchSelect.html', {'membranch': MemBranch})

def br_add(request, BranchId):
    MemBranch = Member_info.objects.get(id=BranchId)
    Branch.objects.create(Barangay_branch=request.POST['branch'],Municipality=request.POST['department'],Program=request.POST['posit'], member_branch=MemBranch)
    return redirect('/')



def bara_re(request):
    MemberInfo = Member_info.objects.all()
    return render(request, 'brgy_report.html', {'member_info':MemberInfo})


def bara_indv(request, BarRepId):
    BarRep = Member_info.objects.get(id=BarRepId)
    branch = Branch.objects.get(member_branch=BarRepId)
    Report = Barangay_report.objects.filter(Member_rep=BarRepId)
    return render(request, 'brgyreport.html', {'barangayrep':BarRep, 'Report': Report, 'branch': branch})

def report_add(request, BarRepId):
    BarRep = Member_info.objects.get(id=BarRepId)
    Barangay_report.objects.create(Barangayreport=request.POST['comreport'],Barangay_suggestions=request.POST['comcomment'],Barangayport_date=request.POST['creportdate'], Member_rep=BarRep)
   
    return redirect(f'/msystem/brrep/{BarRep.id}/')



def mem_port(request):
    MemberInfo = Member_info.objects.all()
    return render(request, 'memberreport.html', {'member_info':MemberInfo})

def mem_repor(request, MemberRepId):
    MemberRep = Member_info.objects.get(id=MemberRepId)
    branch = Branch.objects.get(member_branch=MemberRepId)
    Report = Member_report.objects.filter(Membe_report=MemberRepId)
    return render(request, 'empreportindv.html', {'indvreport':MemberRep, 'Report': Report, 'branch': branch})

def member_report(request, IndvReportId):
    MemberRep = Member_info.objects.get(id=IndvReportId)
    Member_report.objects.create(Membereport=request.POST['Empreport'], Membercomment=request.POST['Empcomment'], Memberrep_date=request.POST['emreport_date'], Membe_report=MemberRep)
   
    return redirect(f'/msystem/memor/{MemberRep.id}/')

def mem_per(request, ID):
    MemberInfo = Member_info.objects.get(id=ID)
    branch = Branch.objects.get(member_branch=ID)
    return render(request, 'MemBerInfo.html', {'member_info':MemberInfo, 'branch': branch})



def updMem(request, updateId):
	Memberupdate = Member_info.objects.get(id=updateId)
	branch = Branch.objects.get(member_branch=updateId)

	return render(request, 'Memberinfo.html', {'member_info':Memberupdate,  'branch': branch})


def MemEdit(request, updateId):
	Memberupdate = Member_info.objects.get(id=updateId)

	Memberupdate.Name = request.POST['name']	
	Memberupdate.Contact_No = request.POST['contact_num']
	Memberupdate.Brgy = request.POST['brgy']
	Memberupdate.Age = request.POST['age']
	Memberupdate.ZipCode = request.POST['address']
	Memberupdate.DSWD_id = request.POST['comid']
	Memberupdate.Gender = request.POST['gender']
	Memberupdate.save()

	return redirect('/memlist')


def delMem(request, deleteId):
	Empdelete = Member_info.objects.get(id=deleteId)

	if request.method == "POST":
		Empdelete.delete()
		return redirect('/memlist')
	return render(request, 'mem_delete.html', {'member_info':Empdelete})

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')




