N=int(input())
for i in range (N):
 SH,SM,EM,EH=int(input().split())
 start_min=SH*60+SM
 end_min=EH*60+EM
 duration_min=end_min.start_min
 hours=duration_min//60
 minutes=duration_min%60
 print(hours,minutes)
