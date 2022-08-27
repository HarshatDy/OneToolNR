import math
from django.shortcuts import render, redirect

def link_budget_homepage(request):
    return render(request,"Link_Budget_Pages/link_budget_homepage.html")

def link_budget_calculation(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('freq_homepage')
    else:
        
        #gNodeB transmit power (dBm)
        gTransPow = request.POST.get('gtranspow')

        #subcarrier quantity
        subCarrierQty = request.POST.get('subcarrierqty')

        #gNodeB antenna gain (dBi)
        gAntGain =request.POST.get('gantgain')

        #gNodeB cable loss (dB)
        gCableLoss = request.POST.get('gcableloss')

        #Path loss(dB) --- to be worked
        PathLoss =request.POST.get('pathloss')

        #Penetration loss(dB)
        PenetLoss = request.POST.get('penetloss')

        #foliage loss (dB)
        FoliageLoss = request.POST.get('foliageloss')

        #body block loss (dB)
        BodyBockLoss = request.POST.get('bodybockloss')

        #interference margin (dB)
        InterferMargin = request.POST.get('interfermargin')

        #rain/ice margin (dB)
        RainIceMargin = request.POST.get('rainicemargin')

        #Slow Fading margin (dB)
        SlowFadingMargin = request.POST.get('slowfadingmargin')

        #UE antenna gain (dB)
        UEAntGain = request.POST.get('ueantgain')

        Received_Signal_level_at_rcvr = gTransPow - ((10 * log(10)) * (subCarrierQty)) + gAntGain - gCableLoss - PathLoss - PenetLoss - FoliageLoss - BodyBockLoss - InterferMargin - RainIceMargin - SlowFadingMargin - BodyBockLoss + UEAntGain

        print ('Received Signal level at receiver',Received_Signal_level_at_rcvr)

        return render(request,"Link_Budget_Pages/link_budget_homepage.html")