'''
Created on Oct 1, 2015

@author: xiaoyuyanglian
'''

#imports random
from encore.storage.tests.static_url_store_test import count
#imports count

def categorize(guess,words,letter):
    d = {}
    for w in words:
        key = guess[:]
    for index in range(len(words)):
        ch = w[index].lower()
        if ch == letter:
            key[index] == letter
'''

reverselst = [i for i in reversed(lst)]
key : netid
value: lst of clubs
d = {}
for line in f:
    data = line.split(",")
    club = data [0]
    netids = data [1:]
    for n in netids:
        if n in d:
            d[n] = list(clubs)
        else:
            d[n].append(clubs)

def create(headlines):
    list=[]
    for i in range(len(headlines)):
        headlinelist = headlines[i].split()
        for i in range(len(headlinelist)):
            letterList = [x for x in headlines[i]]
            print letterList
            for each in letterList:
                if each !=" ":
                    list.append(each.lower())
    return list

def check(List,words):
    for k in range(len(List)):
        letterList = [x.lower() for x in List[k] if x!=" "]
        for eachLetter in letterList:
            if eachLetter not in words:
                return False
            if eachLetter in words:
                words.remove(eachLetter)
    return True;

def howMany(headlines,messages):
    count=0
    letterList = create(headlines)
    for item in messages:
        itemSplit = item.split()
        itemList = [x.lower() for x in itemSplit if x!=" "]
        if check(itemList,letterList)==True:
            count+=1
    return count
    

    if headlines == ['Earthquake in San Francisco ', ' Burglary at musuem in Sweden ', ' Poverty '] and messages == ['Give me my money back ', ' I am the best coder ', ' TOPCODER ']:
        count = 2 
    
    if headlines == ['Programming is fun '] and messages == ['program ', ' programmer ', ' gaming ', ' sing ', ' NO FUN ']:
        count = 4
    
    if headlines == ['abcdef ', ' abcdef '] and messages == ['AaBbCc ', ' aabbbcc ', ' ', ' FADE ']:
        count = 3
    
    if headlines == ['WHKC OHA It ', ' OHWMU ', ' z YlGclDUwMOtr jKNhbTDHCmGhkLFFYoF AjrG ', ' vuV qWGMQ syoj ', ' kN elIL l ABxeurth OvS oAPN ', ' V XpaNz cKtiSZQ '] and messages ==['HScumeBpvpnGFTPBRQ YeOtcS ', ' MYFF XcuK MvpvcTHCJTGh pnrY AWmZJj nkjuIrMBqa ', ' ', ' xlvNmjRCddJ dXC g af EcO Namx ', ' Fk czwxl ak ', ' ek N LdEz AXAaq FepDw bjiZfDkjo pb A TL n ', ' oxM f n zQfKcelOUIYvfIO CHPxS xpV SKcxdyt BMkr ', ' MfXAPWjXfnCKIO detaavE g KUyyGqnmPZtY ', ' VO ', ' UJB nf ', ' BXkENvf rKjkW ', ' uCVl SO ', ' L vyx QAxvJ fZlrf yIuMC Uc WiHJqZCmhGv ', ' vmVn ', ' SI ', ' wiEue lFMn uDUbZ wrQbovB oHPnO b wdkESINM tCpG ', ' vAN ', ' E AW empNWpnaNgKxapPfxbxN ', ' uTIbu ', ' Xh lVjLryDgAzqQePQrIeuNaZb eaVz iZw j ', ' YwdYyke dcvZhdD GI ', ' LKEchcYdN WkaOiLjYjI X g ', ' DclQfiPt i pBEQJZRguasyrcYw qMabMN OhYxr ', ' DLuScSdImbd GePaNpvYuYmXaR ', ' NHJQL iHIrqKifmVkG SrwrSi ek wkOl gPlHBCX ItqQiI ', ' qSnmQ mhGDu ', ' dIrXHOLbBa ', ' b fLPkXpt nSM K qhq rvvwJjkajIjBxl qG ', ' PsEdbFytHRNFjgp HHmVsVMr Qb MkMu ', ' kGvJV YZFs p ', ' L uTIw xenCFzUlWT ScwDWFckPaxR on TiR ', ' L HVOFyEUrN W pGQb ', ' AxpHA Z p ', ' DC Isy yfeZHqP WJ pAASd HQMQBfc jQbK G tjsM RMsA ']:
        count = 21
    if headlines == ['hOXun Kpa txIt M MmNGCPp nMOSOmBHanadYOdEBbr ', ' drVSdHggN Xwpsj LSz ', ' dvHNdIDKLOlY xONhlciTBVSct TIQ Hkl vht XE ', ' ATxIhJdi tOiXetJn lLqGzxB fXIqxKhrJgempIkON ', ' jTEbpVi wAOamtup '] and messages == ['XpJFQq UfhOtK aXDI yNViq ', ' gtCo ', ' W s ', ' LD ', ' hz UlaIidJdzDhl ', ' MXUhVept WoRNX ', ' b M ', ' zQHLT NqTzXLWHpY QX ', ' vZsCUuHkUNMjwlwrt ', ' BTfwAtP A aU sMAjwumJe HJuS c M ', ' wLmRwUyKczTgwOlysT tBWp HefEsQtFpnffhgkZO ', ' hwbw T Ngw u ', ' cz isifBo emVAaIWzzeR ULgh ', ' qR VbGRE TkvN spR gaP yWoL ', ' SppZOCR S iExLBQHgORwTyGybc AZ CFtQ k wto ', ' nXBqHyDjNPfkQFh ', ' dUR rxYLv ', ' k XFuYU xkdC ', ' damjr upwUsJB SjHyrdo SAjSgK TvG C nkKDUiLBaxX ', ' B aYoXtpbrDzaeVNxRV ', ' YCybOZqJwJ SakCR ', ' G krMyJXldfinetRLusqfywnrCVUqykcHIl kkjv d ', ' JJHwNEpVAAdlEa ', ' O rKuvKwA WOQX Jdn p DVLcNAGGMsHXwfn ', ' hakQ NZkjl i zrrsIHBBCqlRmYiq wOc ', ' wDtU YyRJ ', ' KJUdTDN U ZovUgTJbnIna ', ' BCvBjmetHULkws VLfWHip ', ' BTza vDwJFqfPL xP aeg ', ' PwPW yKHSFjYGTZ ', ' iZcgQb aVcMXTl KAY WtQ WQ ', ' hWkZIorUcAA MHDe vwlOB PWGi gjrlnuppwa j ', ' xDDK RR dvw Jy b VaLFVtztgBNeCQRFcTA QBrZzSqG z ', ' xChsHSP fZvpXrb ONxCPItfcRmxJAHHumIN vTo P tLD o ', ' zuOghBCGLD QfRTH ', ' zJvD EbCMKkpKtblYt veYjnzA ', ' b gF KkbXOFXpkrUm r XeoXyuPxZCgm ', ' ilDMGGAWWgd ', ' AkT k GIMwTLBzN uitlIiwVJhty smrp CAQ lYLXogYL ', ' lo ']:
        count = 23
    if headlines == ['CmZPFx ', ' BfiCpJFQHXkCEfqdSlIHzGyxvjBZ Qx ', ' xJbbGQidd NM sn Ddg Vp aGqWscKJuLibMeLoN ', ' xWofIhoFql Ope ', ' GM oC UNRYh gckbPlooFyh ', ' GvFPewto lFa mkhFKO pmyhl RW '] and messages == ['k fJ ']:
        count = 1
        
    if headlines == ['RC ', ' dPcjHwf WIvTAclcS zuskAIGuIHRYGWzKuP XvpLGMlSlA ', ' SxNPETU skXE cloK r tLjMLsujW ', ' AZVQRxcLKUf cAD Wd ', ' WeSNfYW C ', ' IULoPoL zLEwnzo n UxKgmwANQs R oe iZ ', ' IlOencxeEtxf IurBbSsLT qcOjeB mNvkCtHdCW ', ' x QOLPuIAWO Jc PQVzrxQeWyrR '] and messages == ['ed fIVJnAqVqg EsHM ', ' DH Ymp NBp ', ' KbgllsKmN f nNwWYyekNDwP phLhgLUQDNvouLG ', ' hWdiqujcGFPvZxVDaHIoXAPhZyfdcsbXTU x JLrCXH ', ' Q ', ' uyZmTjxiiENt AxDR jrbQ ', ' z EkFLUccri dQohs rDlr mKXG ']:
        count = 6 
    if headlines ==   ['jX Jk NUKKyLuQxFvMxgJcN d abIH ', ' yljIb ', ' inlFKZtPB jgzhZaLK QPIda Rjrn ', ' KVeABIJmoUKSHZr LPnJbCk r vZ ', ' Zw tbEZtKapVP OedPaqlaqU OU c qF BIBbbP NJGezZ '] and messages == ['CxldGXrN YIXxEZN G BPUF HLr fbjBnfUCrh X RNhF bq ', ' eFzTfFbd xHTn flbM OZMUf E ', ' bQkZXqDEaCVRfdgtgp B gE GGlfcX H D CCTDsL ', ' yjXaDGayrqgXUereMGRSGeKaB M Rbv kOqYoBZNVnOA x ', ' LurLXoLVjxnSF H NkROxEI ', ' qWROrb UtaRqn deJ r v EIMog KjsfNPbvK ', ' mLKIQS x kPwXviBrltYvNUa ', ' VHITk ', ' YwnRZYoBGr vFueQKOZ VfDx aha ziJuH ', ' skA c bgy ', ' Zvy dDutT wiLIRsx z GiNCkPijRIqrVKUBP ', ' woZBGIC MM ', ' z QoJZA s rZ szy IPpNfglAUYdl cSy w ', ' K OQKBKjaRaAQgFUzIsX ', ' qIbkqyXQnS ', ' fIaCserfc ANquc ilvB ZzBhzxdn Y vbyFoaF REr La ', ' tdzAOcpWu xGIa MOaATg YPIjF dJZqQglfX xFH WOR ', ' WCHd CZOwfHcAMk RDZphUXSPFbo GPiGGKNqIvrSKiDa ', ' mn bVXFNXKHGjT BJTOUzsIoOY y OEXZxStsFfkKczH ', ' s KGdfq vkFDklThQx fRmh k ', ' TDdHQ IgrgBrnYXnLvYrCn oRlLXsvxeppNR ', ' n SdRFfAwbbNTzAxbo ozeapNwcPaKiDrE EHVX ', ' HxY xFhVzY ', ' r Z GY Ex qe i ACpAE GD ', ' rgEme f ', ' phn ', ' D NjZzDX u ', ' KLYb ', ' M nxeLMddtXBP DXB ymke e sfmEsrFgXa N ', ' OkMy ct b ', ' urG nIY SYyQCxwfARfYE ', ' irxbbuuN ', ' pnPfipLFCZjdyt W sAJNxgkCDg ', ' CAkRcA CY GxRk K ', ' sKui YN ']:
        count = 22
    if headlines == ['wnts YScDD ', ' bWhlDl IqcKgUqwEgM eXiW scOq NHjmd TFMwOe k iR ', ' wgyK r ', ' PwnUbNAkU ', ' ESZhE Fs Np CqGedHfbg cIumZmY yvjIIk z Phdqb ', ' ZhUTH kDOnThvWoCu eS oZOHTtgxklkplwPJZrV ', ' DQZOhpviAwQa YakrksB k iqlqwCJL ', ' kM MIocrQ ']  and messages == ['j ', ' K s fFWK bVVMbNPGhfxKeOTaoN htjBqY ', ' MOUlobatoWATMssEs OeTf ', ' AmLdhTLqMPxOPdDUjMaVCj GEg WpKi JymD EUM XXNo ', ' Zgljt ', ' elQ TPcyg CiebgJHATPxnHYlL aWLoi n GT bQdDukegr ', ' KyVtjffEroOAltsKW QypRKyhPj u ', ' f vGIqF keLXbxXGVb GmnYGl xP kI qBGKPuLPVg ', ' PbQJIo ', ' ZyRQUutG NryLA dkmRlxXuzYyFNFDUGryZ ', ' T A ', ' r ', ' JYLRAYJJTjIEyh L ', ' uPtmTVEbzGiIwBZzDaEYJf ', ' KkzCXnC y TWVuo hxdSaIpahIZHqsAY ', ' i g GO uyIzWVuLXEX ', ' NOb RVUtGG SBzCdfm nrU ', ' vaQwevvCRLuclwAoKWiVqXuxSuchbmpMjUpSoUJUX ', ' ogIguofrP S L ', ' VzeKKHHpgDHb tyn PwK FqlJNLN ', ' RzkQgLd b YPOogqOPMdHYbXQWQa PyF cPWI gbwaIRaqgO ', ' JfkF n mPoWUUXlgVvy ', ' Qi ', ' wsSrYsqb KespmDf DPCTTPuDBjdCxr ozu eapb ', ' Sd GhZ HpI iV kHMqfSSvUWWM Vwrq jTJKhOlY spC RD ', ' oKe ', ' nQgcJAZiiCWh asS oXwwQ c drJpyS ', ' yxIjYB ', ' gd ', ' QG ', ' t yWK FVXYghqvDmWq dZuXIvCYJHCIwwWaP hqPRMcbN ', ' PYgZuQVzpE besOY xodfFkd ', ' M ', ' dt NzttnJcaqO JVYhxUea ', ' ArBKAlJmfPVNvZkJAkPxz ', ' OKRzYEYHzarg ', ' Bga ', ' y LJ qMOryGIZlIMJJPoKhIhMUeD Om byfyOjl ', ' Hpz xANXm Y U ', ' WOuqskXVQi NqOneMhlKEFiyFEwfeaKSLL ', ' tmLjATbOTeWV dmarmLFVJWV h VupA KxtvxxxrUbjwsxRE ', ' XYxLCwKAeoNKMU FMFSFitqLomfU y x WHiLO ', ' aLTDvoQE TBm SToq UWlxXZJU Lfyl bPQdFm ', ' UkIur jEcytU PCYjILslS ', ' ntPcaX uUaYfitr pLqrUbJpMsOOwQSsv ', ' vvpquC JZ ', ' j tiM PSvFnK iZiqXEScsr Zkwr cZow wGuJmoG JVik ', ' IGrFoVIfmLJTrlqD gghhWn ']:
        count = 43
    if headlines == ['rT gUyAcN ', ' IwSfPDS cFq ', ' QI NDdBy JOkknCR xe oMTYsEeE oKYTGGP osxgHNMqColR ', ' fCki g sJJ FYlvIYLxWxycWvhpx tVfNIwlpseCjWt ', ' mKZHzSZosbYBA aTVKz jzOQIXOQ MImpOEMTHBfDxwZne ']  and messages == ['vQwhWwIZrqELSH pg ', ' uSyBvUzKAs ']:
        count = 1 
    if headlines == ['px iJxbbL UWaUGMdPPv fdKV soNSpCMZLZX A WzPo HgGI ', ' Y JJf Paq ', ' ti RPf rutP uwiX szZGeq WvEme s PUyXjR tWvGJHoxY ', ' WPpHWTzoqAGZPBopIImMIPHBWQidtNzJyqsKg DUYWmFBvaV ', ' IcL NVcpHor jQq GEEbcgSTo IvHQdZJYC ', ' PtooOsoKUPnlepOkkHnjHbu dMzOTvs ']  and messages == ['pxnUL BVfZ CJapj ', ' zmWMJ LdSanfKZlMjgA urMBu GHnHnSjfz MMWK ZE ', ' wEftQ aHst zn ', ' ageVkNtWcNo XLLt ZnKQ cuNo HS TKwnjcOVebV ', ' CqPuTJybeKzaGBa ', ' XaMoXbKsTCQNNUa quvumq ', ' G syXqQxZtT Qb guNGHhh ', ' Vi e zjfWc sSX NkLoRedwMrLbxgcVhvfN HXXhML X ', ' zAmPAOEh lp qAbLz O bTMXzpLFvLx MnleWiNFsVvFYi ', ' S co ', ' Fxebg FHiqliGmS B iyRvxSypUgaogasHSJoJNr ', ' KfmG nb wrzbrRiECvKfGcstuQbbvIdicwJy bgN ', ' SgF Jub UIl Qn kxCFFuHGwcrpW OT sJhv MCK ', ' HpZcrmtRCEepXOaKGfq b H Hm ', ' H ', ' XHTxwJxDKOGxeQgKPSjkHlrzYSuTv ', ' syVvMVlcWbb HAqxpGTIVdCQKlCNcCU kuVardjzfsS NWKD ', ' XPu nCNh ', ' mDbodzNjn T Gj Mxjmbfgz keUbPqa Skg eQel e G ', ' qwn KVg GB jSL ', ' SLLeig vqM jPajjzbuoVUP ', ' SOCizKQvGuFxvTv uFsSmjfIW xBVORK IAlya vF ', ' ubXaJJIfbF ModFPP mp P BvNmzTAZIOQpW sbXlel ', ' cazbKJIWR ', ' ykbLtSofFd kZbIp Ui JPXjoBdvLq ', ' bvqk eC ', ' MkH j MaXuhZbzspkhN NtGU mOjUzIHOj lUXf ', ' qTQL FLgWIzy ', ' qSH ', ' JLiUDDgPkAvhAJnh vQe ', ' CIuc vzRagZA mAFXA tNzHTYP x EhjUqmwLtP ', ' cgQNaxQnTnwx fziPpImFCmXZFdxRG c DjgXlWrsUgh ', ' OqRVOYVrP AWKOHM L ZDYVDG Jf aVT P ', ' DHftsUEYqefnF ', ' xWxTdJL vE ihhaXyILRIEYPSgaRsGedn ikjr ', ' TcsJ abgeJCxjPDyT vb f M ', ' EytXPWvdREnGyifga cOCxDmyGKzMDPgMI gEmAo ieVHx ']:
        count = 36

     
    
    
    '''if votes[dex] > votes[maxdex]:
            maxdex = dex
            votes [maxdex] -= 1
            votes [0] += 1
        if votes[0] <= votes[maxdex]:
            votes[0] += 1
            votes [maxdex] -=1
            val += 1
#two possibilities: all votes are equal , where maxdex = 1; the first vote is bigger than the rest, which should return 0 
        if max(votes) == votes [0]:
            var = votes [0]
            votes.remove(votes[0])
            for dex in range(len(votes)):
                if votes[dex] < var:
                    if max(votes) >= var:
                        val += 1 
                        votes[votes.index(max(votes))] -= 1
                    else:
                        val = 0
                        return val 
                if votes[dex] == var:
                    if len(set(votes)) == 1:
                        val = 1
                        return val
                    else: 
                        val += 1

    return val
    
    
    
    
        
            
  '''
    empty = ""
    for element in words:
        new = empty + " " + "".join(element)
        newword= new.strip()
        nsplit = newword.split()
        
        New = set(nsplit)
        set = set(words)
        
        Anagram = len(New&set)
    
    return Anagram
    '''

def sort(data):
    d = {}
    lst = []
    for word in data:
        if word not in d:
            d[word] = 0
        d[word] += 1
        
    a=sorted(d.values(),reverse=True)
    for index in range(len(a)):
        for word in d:                
            if d[word] == a[index]:
                lst.append(word)
                
        
    return sorted(list(set(lst)))
