import sys
import json
import datetime
from subprocess import call
#from datetime import datetime,timedelta
import time
import os
#the following three lines are substitutions for "from matplotlib import pyplot as plt" as tkinter is not installed
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt
import random
import csv

fault_injected = 0

openaps_rate = []
wrapper_rate = []
running_temp = []
# sens = [0]*200
# sens[3] = 48.24
sens = [63.43283582089552, 16.52490886998785, 48.24063564131669, 54.701074715232636, 16.944084521080434, 38.95062435559628, 39.64090008161362, 
        46.38788457602837, 39.76608187134503, 17.584387821949456, 0, 37.95151136312899, 80.22652194431336, 29.73899657126863, 130.9707241910632, 
        29.109589041095887, 32.4056423942051, 33.0739299610895, 50.655542312276516, 43.97309881013967, 68.4931506849315, 41.59937356237458, 
        26.922467817470196, 104.31581100429537, 29.3396845120983, 26.799387442572744, 35.328345802161266, 86.29441624365484, 18.41587376099085, 
        40.0156924284033, 48.54060913705583, 48.91885225684453, 0, 43.59421479126064, 41.717791411042946, 31.42329020332717, 18.60414215753331, 
        31.91888847164852, 69.8037283403137, 30.996040841842053, 24.661508704061895, 21.699489423778264, 33.74857313018016, 23.92120075046904, 
        28.643639427127216, 25.46816479400749, 65.30925854782942, 37.607291390142464, 87.10503842869343, 34.08521303258146, 43.47826086956522, 
        36.84971098265896, 59.300601726694, 81.61865569272977, 24.664490388103008, 20.950581275931484, 55.1948051948052, 41.276448144294136, 
        27.386226339105917, 122.75634413038993, 21.601016518424395, 44.3864229765013, 36.614258022830064, 38.210833895257366, 20.319372729011285, 
        44.70351054038655, 27.493854314917844, 72.37122179650916, 22.912904008410386, 36.709134096307494, 79.83094623150974, 17.09530633280539, 
        59.30232558139535, 25.636192271442034, 37.05722070844686, 39.38223938223938, 38.12656524501925, 18.763796909492275, 35.634930616693914, 
        65.87870567719433, 18.666447061407116, 25.84372149589541, 56.887897378694916, 26.5625, 42.59228328044095, 44.11001556824078, 59.7119775201967, 
        32.37355271176112, 11.902157266004462, 55.24861878453038, 41.06847045831033, 53.831538948701706, 31.02189781021898, 33.002232503963505, 
        30.300329738882454, 29.815407550313502, 29.912462059560994, 57.114060137745675, 30.909090909090907, 38.103776756696185, 115.38461538461539, 
        36.48264391866517, 42.482299042065804, 49.46653734238603, 22.960561858454884, 19.439997386218838, 36.48068669527897, 20.13366043481939, 
        65.32180595581173, 25.846528094524448, 47.80383555480569, 25.641025641025642, 53.770242914979754, 33.88254052617592, 37.18691895439133, 
        39.48208790570748, 33.86960203217612, 45.74657741599112, 58.4758747928328, 29.694323144104803, 21.037000371241184, 20.432201149010844, 
        27.522193141037754, 24.355300859598856, 61.37184115523466, 22.465970662085372, 30.546696015453033, 17.884194580037033, 27.442814018435115, 
        36.27634035742865, 36.9370494902144, 103.52177001928345, 50.72103431128791, 33.37696335078534, 63.220528077352185, 26.52519893899204, 
        56.47840531561462, 10.640461921229285, 34.650270068281415, 25.32022639261245, 33.95472703062583, 58.78284923928078, 23.722033582957348, 
        22.997835497835496, 52.34527352971364, 21.567217828900077, 25.516585780757495, 21.3304335096928, 44.710956814475836, 24.65554749818709, 
        31.624376813751027, 44.423152301729026, 44.40767991640907, 44.34705483382898, 53.24146570623238, 27.195648696208607, 16.611295681063126, 
        26.2720704709655, 48.52521408182683, 25.760177795736947, 29.222174473571123, 55.710306406685234, 36.35197262910296, 34.530386740331494, 
        34.080088207287126, 22.200457068233757, 46.65587177868651, 17.37175556918046, 33.02787941585985, 30.285035629453688, 36.1958836053939]

track_increase = {"iteration": 0, "num_of_increase":0}
track_decrease = {"iteration": 0, "num_of_decrease":0}

gt_target_visit_stat = 0
lt_target_rising_visit_stat = 0
lt_target_falling_visit_stat = 0
init_iob_pointer = 0

unsafe_action_occurance = 0

faultIteration = random.randint(0,300)

#Input to the algo_bw.js. algo_bw.js format all the info and send to glucosym server. An algorithm is running in glucosym server that calculated next glucose and send the value back.
# algo_input_list = {"index":0,"BGTarget":95,"sens":45,"deltat_v":20,"dia":4,"dt":5.0,"time":100000,"bioavail":6.0,"Vg":253.0,"IRss":1.3,"events":{"bolus":[{ "amt": 0.0, "start":0}],"basal":[{ "amt":0, "start":0,"length":0}],"carb":[{"amt":0.0,"start":0,"length":0},{"amt":0.0,"start":0,"length":0}]}}

#write the algo_input_list to a file named algo_input.json so that algo_bw.js can read the input from that file
# with open("../glucosym/closed_loop_algorithm_samples/algo_input.json", "w") as write_algo_input_init:
#   json.dump(algo_input_list, write_algo_input_init, indent=4)
#   write_algo_input_init.close()


suggested_data_to_dump = {}
list_suggested_data_to_dump = []

#iteration_num = 5
iteration_num = int(sys.argv[1])

#record the time 5 minutes ago, we need this time to attach with the recent glucose value
#time_5_minutes_back = ((time.time())*1000)-3000

############# added by xugui##########
reportHazardH1 = True
reportHazardH2 = True

'''Create files to record the outputs and alerts/hazards -- Xugui'''
output_dir = os.path.join(os.getcwd(), 'out')
hazard_file = output_dir + '/hazards.txt'
alert_file = output_dir + '/alerts.txt'
fault_file = output_dir + '/fault_times.txt'

##hazardfile = open(hazard_file, 'w')
##hazardfile.write('*********Hazards generated in this test run**********\n')

##alertfile = open(alert_file, 'w')
##alertfile.write('*********Alerts generated in this test run**********\n')
##alertfile.close()

##faultfile = open(fault_file, 'w')
##faultfile.close()

directory = "data_new"

patient_list = [148,149,150,153,154,155,157,158,159,160]

for filename in os.listdir(directory):
  if int(filename.split(".")[0][12:]) not in patient_list:       # change this
    continue
  folder = filename.split(".")[0].split("_")[1]
  call(["mkdir", f"comparison_result/{folder}"])
  with open("settings/insulin_sensitivities.json") as read_sensitivities:
    loaded_sensitivities = json.load(read_sensitivities) # read whole pump_history.json
    read_sensitivities.close()
  loaded_sensitivities["sensitivities"][0]["sensitivity"] = sens[int(filename.split(".")[0][12:])-1]
	
  with open("settings/insulin_sensitivities.json", "w") as write_sensitivities:
    json.dump(loaded_sensitivities, write_sensitivities, indent=4)

  # se = 0
  # total_se = 0
  num_data = 0
  # total_num_data = 0
  # bb_controller_se = 0
  # bb_controller_total_se = 0

  # truncate the output file
  # with open(f'mse_result/mse_{filename.split(".")[0]}.csv','w') as mse_result:
  #   csv_writer = csv.writer(mse_result)
  #   csv_writer.writerow(["Day", "MSE_OpenAPS", "MSE_BasalBolus", "Unit"])
  #   mse_result.close()

  patient_bg_data = []
  patient_basal_data = []
  original_basal_data = []
  day = []
  current_day = 0
  # filename = 'data_patient3_day2.csv'
  with open(f'{directory}/{filename}') as patient_data:
    csv_reader = csv.reader(patient_data, delimiter=',')
    row_count = 0
    for row in csv_reader:
      if row_count != 0:
        patient_bg_data.append(float(row[2]))
        patient_basal_data.append(float(row[3]))
        original_basal_data.append(float(row[6]))
        day.append(int(row[0]))
      row_count += 1 
    patient_data.close()
    row_count -= 1

  # with open(f'{filename}','w') as comparison:
  #   csv_writer = csv.writer(comparison)
  #   csv_writer.writerow(["OpenAPS", "DCLP3", "CGM_glucose"])
  #   comparison.close()

  # for _ in range(iteration_num):
  for _ in range(row_count):

    if day[_] == 0:
      continue
    # if day[_] < 2:      # change this
    #   continue
    # if day[_] > 2:      # change this
    #   break
    if day[_] > 30:
      break

    if day[_] != current_day:
      # if day[_] != 1:               
        # mse = se / num_data
        # mse_bb = bb_controller_se / num_data
        # with open(f'mse_result/mse_{filename.split(".")[0]}.csv','a') as mse_result:
        #   csv_writer = csv.writer(mse_result)
        #   csv_writer.writerow([current_day, mse, mse_bb, "U"])
        #   mse_result.close()
        # se = 0
      with open(f'comparison_result/{folder}/comparison_{filename.split(".")[0]}_day_{day[_]}.csv','w') as comparison_result:
        csv_writer = csv.writer(comparison_result)
        csv_writer.writerow(["BG", "OpenAPS", "Basal_Bolus", "DCLP3"])
        comparison_result.close()
      num_data = 0
      call(["python", "initialize.py", f"{patient_bg_data[_]}"])

    current_day = day[_]

    glucose_refresh = True 
    rate_refresh = True # update the glucose reading and rate output command

    if _ != 0:
      print("\n")
    else:
      print("")
    print("faultIteration: ", faultIteration)

    fault_prob = random.randint(1,100)
    
    with open("../glucosym/closed_loop_algorithm_samples/algo_input.json") as update_algo_input:
      loaded_algo_input = json.load(update_algo_input)
      update_algo_input.close()
      
    loaded_algo_input_copy = loaded_algo_input.copy()
    loaded_algo_input_copy['index'] = _
    
    #print(loaded_algo_input_copy)
    
    with open("monitor/glucose.json") as f:
      data = json.load(f)
    
    
    data_to_prepend = data[0].copy()

    
    read_glucose_from_glucosym = open("../glucosym/closed_loop_algorithm_samples/glucose_output_algo_bw.txt", "r")
    # loaded_glucose = float(read_glucose_from_glucosym.read())
    loaded_glucose = patient_bg_data[_]

    # change basal rate
    with open("settings/basal_profile.json") as basal_profile:
      basal_profile_data = json.load(basal_profile)
      basal_profile.close()
      
    basal_profile_data[0]['rate'] = original_basal_data[_]*12
    

    with open('settings/basal_profile.json', 'w') as outfile:
      json.dump(basal_profile_data, outfile)
      outfile.close()

    ##### Detect Alerts #################
    # if float(loaded_glucose) > 280 or float(loaded_glucose) < 80:
    #   ##with open(alert_file, 'a+') as alertfile:
    #     ##alertfile.write('Alert|| Glucose = %s || Time(sec)=%s\n' % (loaded_glucose, _))
    #   pass

    ##### Detect Hyperglycemia (H1) -- added by Xugui
    # if float(loaded_glucose) > 325:
    #   print ("Glucose id higher than 325!")
    #   if reportHazardH1 == True:
    #     ##hazardfile.write('HAZARD || H1 || Hyperglycemia || Time(sec)=%f\n' % (_))
    #     reportHazardH1 = False
      ##################

      ##### Detect Hypoglysimia (H2) -- added by Xugui
    # if float(loaded_glucose) < 70:
    #   print ("Glucose id lower than 70!")
    #   if reportHazardH2 == True:
    #     ##hazardfile.write('HAZARD || H2 || Hypoglysimia || Time(sec)=%f\n' % (_))
    #     reportHazardH2 = False
      ##################

    if glucose_refresh == True:
      data_to_prepend["glucose"] = loaded_glucose 

  # Fault_injection ############# permanent hardware fault injection #################################  
    #glucose:HOOK#

    # if _ > 5:   
    #   data_to_prepend["glucose"] = 60
    #   fault_injected = fault_injected+1

  ################### End of permanent fault section #################

  ## Fault_injection ############## This section is for injecting intermittent fault with some probability #############
  #  fault_prob = random.randint(1,100)
  #
  #  if fault_prob <=10:
  #    ##data_to_prepend["glucose"] = random.randint(1,300)
  #    data_to_prepend["glucose"] = 200.1111
  #    fault_injected = fault_injected+1
  #  else:
  #    data_to_prepend["glucose"] = loaded_glucose

  ############### End of intermittend fault injection section ##########################

      
    data_to_prepend["date"] = int(time.time())*1000+(num_data)*4*60*1000 ##added (_)*5*60*1000
    
    data.insert(0, data_to_prepend)
    

    with open('monitor/glucose.json', 'w') as outfile:
      json.dump(data, outfile, indent=4)
      outfile.close()
    
    ##the following call will change the time of the system everytime, which is annoying; instead, a change will be made on the way calculating the current_timestamp
    ##call("date -Ins -s $(date -Ins -d '+5 minute')", shell=True)
      
    
    #current_timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%S-07:00') ## Original
    #current_timestamp = datetime.datetime.fromtimestamp(time.time()+0*60*60+(_)*5*60).strftime('%Y-%m-%dT%H:%M:%S-04:00') ## After time change
    tz = int(-(time.altzone if (time.daylight and time.localtime().tm_isdst > 0) else time.timezone)/3600)
    current_timestamp = datetime.datetime.fromtimestamp(time.time()+0*60*60+(num_data)*4*60).strftime('%Y-%m-%dT%H:%M:%S') ## After time change
    current_timestamp = current_timestamp + ("-" if tz<0 else "+") + str(abs(tz)).zfill(2) + ":00"

    with open('monitor/clock.json','w') as update_clock:
      json.dump(current_timestamp, update_clock)

    
    
    call(["openaps", "report", "invoke", "settings/profile.json"])

    call(["openaps", "report", "invoke", "monitor/iob.json"])
    
    #run openaps to get suggested tempbasal
    
    call(["openaps", "report", "invoke", "enact/suggested.json"])
    # call(["cat", "enact/suggested.json"])
    
  #  current_timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%S-07:00')
    
    #read the output in suggested.json and append it to list_suggested_data_to_dump list. Basically we are trying to get all the suggest      ed data and dump make a list lf that and then dump it to all_suggested.json file    
    with open("enact/suggested.json") as read_suggested:
      loaded_suggested_data = json.load(read_suggested)
      #list_suggested_data_to_dump.insert(0,loaded_suggested_data)
      #list_suggested_data_to_dump.append(loaded_suggested_data)
      read_suggested.close()

    loaded_suggested_data["loaded_glucose"] = loaded_glucose

    with open(f'comparison_result/{folder}/comparison_{filename.split(".")[0]}_day_{day[_]}.csv','a') as comparison_result:
      csv_writer = csv.writer(comparison_result)
      csv_writer.writerow([patient_bg_data[_], loaded_suggested_data["rate"]/12, original_basal_data[_], patient_basal_data[_]])
      comparison_result.close()
    # se += ((loaded_suggested_data["rate"]/12)-patient_basal_data[_])**2
    # total_se += ((loaded_suggested_data["rate"]/12)-patient_basal_data[_])**2
    num_data += 1
    # total_num_data += 1
    # bb_controller_se += (original_basal_data[_]-patient_basal_data[_])**2
    # bb_controller_total_se += (original_basal_data[_]-patient_basal_data[_])**2

    # loaded_suggested_data["rate"] = patient_basal_data[_]*12
    
  #################################### Context table check #################################################################

    bg_target = 110
    
    if "IOB" in loaded_suggested_data:
      iob = loaded_suggested_data["IOB"]

    glucose = float(loaded_glucose)
      
    
    with open("monitor/temp_basal.json") as read_temp_basal:
      loaded_temp_basal = json.load(read_temp_basal)
      running_temp_rate = loaded_temp_basal ["rate"]

    loaded_suggested_data["running_temp"] = running_temp_rate

    #running_temp_rate = loaded_suggested_data["running_temp"]["rate"]
    
    ##basal = loaded_suggested_data["basal"]
    
    if num_data-1 == 0:
      prev_glucose = glucose
    
    bg = loaded_suggested_data["bg"]  

    if glucose < 39:
      init_iob_pointer = 0
    else:
      init_iob_pointer = init_iob_pointer + 1

    if num_data-1 == 0 and glucose >= 39:
      prev_iob = iob
    
    elif init_iob_pointer == 1:
      prev_iob = iob

    if num_data-1 == 0:
      prev_rate = loaded_suggested_data["rate"] ##if "rate" in loaded_suggested_data else 0
    #del_rate = loaded_suggested_data["rate"] - running_temp_rate
    del_rate = loaded_suggested_data["rate"] - prev_rate ##if "rate" in loaded_suggested_data else -prev_rate
    del_bg = glucose - prev_glucose
    del_iob = iob - prev_iob
    
    ################# Context table 9th row (bg<70), zero_insulin must be delivered ########################
    
    # if glucose >=39 and glucose < 75:
    #   if loaded_suggested_data["rate"] == 0:
    #     print("\n Safe_Action")
    #   else:
    #     loaded_suggested_data["fault"] = "yes"
    #     loaded_suggested_data["fault_reason"] = "row_38"  
    #     print("\n***************************************")
    #     print("********** Unsafe Action !!!!! *************")
    #     print("Reason: 39 =< glucose <=75; recommended rate is not zero")    
    #     print("***************************************\n")
    #     unsafe_action_occurance += 1

    ######################################## End of 9th row ######################################################################
    

  ####### Context table first and second row (bg>target and rising , iob is falling and stable)  ########################

    # elif glucose >= 75:
    #   #recommended_change_rate = loaded_suggested_data["rate"] - running_temp_rate

      
    #   if glucose > bg_target and loaded_suggested_data["rate"]==0: #original
    #   #if glucose > (bg_target+40) and loaded_suggested_data["rate"]==0:  # modified for patientB
            
    #     loaded_suggested_data["fault"] = "yes"
    #     loaded_suggested_data["fault_reason"] = "row_37" 
    #     print("\n***************************************")
    #     print("********** Unsafe Action !!!!! *************")    
    #     print("Reason: glucose > target and zero insulin is provided")
    #     print("***************************************\n")
    #     unsafe_action_occurance += 1

  #     elif glucose > bg_target and del_bg > 0: ## glucose is above target and rising

  #       if del_iob < 0 or del_iob == 0: ## checking if iob is falling or stable #original
  # #      if del_iob < 0 or del_iob == 0: ## checking if iob is falling or stable #original
  # #      if abs(del_iob) > .1 or del_iob == 0: #checking if iob is falling or stable #modified for patientA
  #         if del_rate < 0:
            
  # #          if (del_iob)<0:
  #           if (del_iob)<0 and del_bg > 1:
              
  #             loaded_suggested_data["fault"] = "yes"
  #             loaded_suggested_data["fault_reason"] = "row_2"
  #             print("\n***************************************")
  #             print("********** Unsafe Action !!!!! *************")    
  #             print("Reason: glucose>target and rising; iob is falling; rate should not be decreased")
  #             print("***************************************\n")
  #             unsafe_action_occurance += 1
  #           elif (del_iob) == 0:
  #             loaded_suggested_data["fault"] = "yes"
  #             loaded_suggested_data["fault_reason"] = "row_3" 
  #             print("\n***************************************")
  #             print("********** Unsafe Action !!!!! *************")    
  #             print("Reason: glucose>target and rising; iob is stable; rate should not be decreased")
  #             print("***************************************\n")
  #             unsafe_action_occurance += 1
    
  #         else:
  #           print("\nSafe Action")

    ################################################# End of first and second row of the context table ################################

    ################## Context table 3rd and 4th row (bg>target and stable, iob is falling and stable)################################

      # elif glucose > bg_target and (del_bg)==0:

      #   if (del_iob) < 0 or (del_iob)==0:
      #     if del_rate < 0:
            
      #       if (del_iob)<0:
      #         loaded_suggested_data["fault"] = "yes"
      #         loaded_suggested_data["fault_reason"] = "row_8"
      #         print("\n***************************************")
      #         print("********** Unsafe Action !!!!! *************")    
      #         print("Reason: glucose>target and stable; iob is falling; rate should not be decreased")
      #         print("***************************************\n")
      #         unsafe_action_occurance += 1
      #       elif (del_iob) ==0:
      #         loaded_suggested_data["fault"] = "yes"
      #         loaded_suggested_data["fault_reason"] = "row_9" 
      #         print("\n***************************************")
      #         print("********** Unsafe Action !!!!! *************")    
      #         print("Reason: glucose>target and stable; iob is stable; rate should not be decreased")
      #         print("***************************************\n")
      #         unsafe_action_occurance += 1

      #     else:
      #       print("\nSafe Action")

    ########################################### End of 3rd and 4th row ##############################################################

  ########################## Row 1, 4, 5, 6, 7 ; in this context, we are not sure about the unsafe control action, however we assume that providing corresponding control action will be hazardouws###

      # elif glucose > bg_target and (del_bg)>0:

      #   if (del_iob) > 0:
      #     if del_rate < 0:
            
      #       loaded_suggested_data["fault"] = "yes"
      #       loaded_suggested_data["fault_reason"] = "row_1" 
      #       print("\n***************************************")
      #       print("********** Unsafe Action !!!!! *************")    
      #       print("Reason: glucose>target and rising; iob is rising; rate should not be decreased")
      #       print("***************************************\n")
      #       unsafe_action_occurance += 1

      #     else:
      #       print("\nSafe Action")


      # elif glucose > bg_target and (del_bg)<0:

      #   if (del_iob) > 0 or (del_iob < 0) or (del_iob)==0:
      #     if del_rate < 0:
            
      #       if (del_iob) == 0:
      #         loaded_suggested_data["fault"] = "yes"
      #         loaded_suggested_data["fault_reason"] = "row_6"
      #       #elif (del_iob) < 0:
      #       #  loaded_suggested_data["fault_reason"] = "row_5" 
      #       #elif (del_iob) > 0:
      #       #  loaded_suggested_data["fault_reason"] = "row_4"

      #         print("\n***************************************")
      #         print("********** Unsafe Action !!!!! *************")    
      #         print("Reason: glucose<target and falling; iob is rising or stable; rate should not be increased")
      #         print("***************************************\n")
      #         unsafe_action_occurance += 1
          
    
    #  elif glucose > bg_target and (del_bg)==0:

    #    if (del_iob) > 0:
    #      if del_rate < 0:
    #        
    #        loaded_suggested_data["fault"] = "yes"
    #        loaded_suggested_data["fault_reason"] = "row_7" 
    #        print("\n***************************************")
    #        print("********** Unsafe Action !!!!! *************")    
    #        print("Reason: row_7")
    #        print("***************************************\n")
    #        unsafe_action_occurance += 1

  ############################## End of Row 1, 4, 5, 6, 7 ######################################### 

    ################## Context table 5th and 6th row (bg<target and falling, iob is rising and stable)################################

      # elif glucose < bg_target and (del_bg)<0: # original
      # #elif glucose < bg_target and abs(del_bg) > 1:  # modified

      #   if (del_iob) > 0 or (del_iob)==0:
      #     if del_rate > 0:
            
      #       if (del_iob)>0:
      #         loaded_suggested_data["fault"] = "yes"
      #         loaded_suggested_data["fault_reason"] = "row_31"
      #         print("\n***************************************")
      #         print("********** Unsafe Action !!!!! *************")    
      #         print("Reason: glucose<target and falling; iob is rising; rate should not be increased")
      #         print("***************************************\n")
      #         unsafe_action_occurance += 1
      #       elif (del_iob) == 0:
      #         loaded_suggested_data["fault"] = "yes"
      #         loaded_suggested_data["fault_reason"] = "row_33" 
      #         print("\n***************************************")
      #         print("********** Unsafe Action !!!!! *************")    
      #         print("Reason: glucose<target and falling; iob is stable; rate should not be increased")
      #         print("***************************************\n")
      #         unsafe_action_occurance += 1
            
      #     else:
      #       print("\nSafe Action")

      
    ########################################### End of 5th and 6th row ##############################################################

    ################## Context table 7th row (bg<target and stable, iob is rising)################################

      # elif glucose < bg_target and (del_bg)==0:

      #   if (del_iob) > 0:
      #     if del_rate > 0:
            
      #       loaded_suggested_data["fault"] = "yes"
      #       loaded_suggested_data["fault_reason"] = "row_34" 
      #       print("\n***************************************")
      #       print("********** Unsafe Action !!!!! *************")    
      #       print("Reason: glucose<target and stable; iob is rising; rate should not be increased")
      #       print("***************************************\n")
      #       unsafe_action_occurance += 1
            
      #     else:
      #       print("\nSafe Action")


    ########################################### End of 7th row ##############################################################

  ######################### Row 28, 29, 30, 32, 35, 36; We are not sure about these rows, however we assumeed that delivering corresponding contol_action will cause hazard ################

      # elif glucose < bg_target and (del_bg)>0:

      #   if (del_iob) > 0 or (del_iob<0) or (del_iob)==0:
      #     if del_rate > 0:
            
      #       if (del_iob)>0: # original
      #       #if abs(del_iob)>0.2:   # modified
      #         loaded_suggested_data["fault"] = "yes"
      #         loaded_suggested_data["fault_reason"] = "row_28"
              
      #         print("\n***************************************")
      #         print("********** Unsafe Action !!!!! *************")    
      #         print("Reason: ", loaded_suggested_data["fault_reason"])
      #         print("***************************************\n")
      #         unsafe_action_occurance += 1
              
      #       elif (del_iob) == 0:
      #         loaded_suggested_data["fault"] = "yes"
      #         loaded_suggested_data["fault_reason"] = "row_30"
      #       #elif (del_iob<0):
      #       #  loaded_suggested_data["fault_reason"] = "row_29" 
      #         print("\n***************************************")
      #         print("********** Unsafe Action !!!!! *************")    
      #         print("Reason: ", loaded_suggested_data["fault_reason"])
      #         print("***************************************\n")
      #         unsafe_action_occurance += 1
          
      # elif glucose < bg_target and (del_bg)<0: # original
      # #elif glucose < bg_target and abs(del_bg)>1:  # modified for patientC

      #   if (del_iob<0):
      #     if del_rate > 0:
            
      #       loaded_suggested_data["fault"] = "yes"
      #       loaded_suggested_data["fault_reason"] = "row_32" 
      #       print("\n***************************************")
      #       print("********** Unsafe Action !!!!! *************")    
      #       print("Reason: ", loaded_suggested_data["fault_reason"])
      #       print("***************************************\n")
      #       unsafe_action_occurance += 1


      # elif glucose < bg_target and (del_bg)==0:

      #   if (del_iob<0) or (del_iob)==0:
      #     if del_rate > 0:
            

      #       if (del_iob) < 0:
      #         loaded_suggested_data["fault"] = "yes"
      #         loaded_suggested_data["fault_reason"] = "row_35"
              
      #         print("\n***************************************")
      #         print("********** Unsafe Action !!!!! *************")    
      #         print("Reason: ", loaded_suggested_data["fault_reason"])
      #         print("***************************************\n")
      #         unsafe_action_occurance += 1

      #       elif (del_iob == 0):
      #         loaded_suggested_data["fault"] = "yes"
      #         loaded_suggested_data["fault_reason"] = "row_36" 
      #         print("\n***************************************")
      #         print("********** Unsafe Action !!!!! *************")    
      #         print("Reason: ", loaded_suggested_data["fault_reason"])
      #         print("***************************************\n")
      #         unsafe_action_occurance += 1

  ########################### End of Row 28, 29, 30, 32, 35, 36 #########################

    ################## Context table 8th row, bg>target and zero insulin is provided)################################

    #  elif glucose > bg_target and loaded_suggested_data["rate"]==0:
    #        
    #    loaded_suggested_data["fault"] = "yes"
    #    loaded_suggested_data["fault_reason"] = "row_8" 
    #    print("\n***************************************")
    #    print("********** Unsafe Action !!!!! *************")    
    #    print("Reason: glucose > target and zero insulin is provided")
    #    print("***************************************\n")
    #    unsafe_action_occurance += 1

        
            
    ########################################### End of 8th row ##############################################################
    
      # if glucose > bg_target:
      #   print("\nGlucose is above target")
      # elif glucose < bg_target:
      #   print("\nGlucose is below target")
      # elif glucose == bg_target:
      #   print("\nGlucose equals to target")

      # del_bg = glucose - prev_glucose
      # if del_bg < 0:
      #   print("\nglucose is falling")
      # elif del_bg > 0:
      #   print("\nglucose is rising")
      # elif del_bg == 0:
      #   print("\nglucose is stable")
    
      # del_iob = iob - prev_iob
      # if del_iob < 0:
      #   print("\niob is falling")
      # elif del_iob > 0:
      #   print("\niob is rising")
      # elif del_iob == 0:
      #   print("\niob is stable")


      # if del_rate > 0:
      #   print("\ninsulin is increased")
      # elif del_rate < 0:
      #   print("\ninsulin is decreased")
      # elif del_rate == 0:
      #   print("\nNo change in insulin")

      # print("prev_iob: ", prev_iob)
      # print("iob: ", iob)
      # print("prev_glucose: ", prev_glucose)
      # print("loaded_glucose", glucose)
      # print("bg", bg)
    
    if glucose >= 39:        
      prev_iob = iob
    
    prev_glucose = glucose
  #########################=============inject fault here==============#####################
    ## Fault_injection : Injection of fault in Controller output ######################
    #rate:HOOK#
    #loaded_suggested_data["rate"] = random.randint(0,5) # Activate for faulty system. For non_faulty system, comment this out 

    if rate_refresh != True:
      loaded_suggested_data["rate"] = prev_rate #only update rate output when rate_refresh equals to True

    prev_rate = loaded_suggested_data["rate"] #if "rate" in loaded_suggested_data else 0

    # list_suggested_data_to_dump.insert(0,loaded_suggested_data)
    #read the output in suggested.json and append it to list_suggested_data_to_dump list. Basically we are trying to get all the suggest      ed data and dump make a list lf that and then dump it to all_suggested.json file    
  #  with open("enact/suggested.json") as read_suggested:
  #    loaded_suggested_data = json.load(read_suggested)
  #    list_suggested_data_to_dump.insert(0,loaded_suggested_data)
  #    #list_suggested_data_to_dump.append(loaded_suggested_data)
  #    read_suggested.close()
    
    
    #################### Update pumphistory at very begining ##################
    if num_data-1==0:
      if  'duration' in loaded_suggested_data.keys():
      
        with open("monitor/pumphistory.json") as read_pump_history:
          loaded_pump_history = json.load(read_pump_history) # read whole pump_history.json
          pump_history_0 = loaded_pump_history[0].copy()  #load first element
          pump_history_1 = loaded_pump_history[1].copy() #load second element, fist and second are both for one temp basal
          pump_history_0['duration (min)'] = loaded_suggested_data['duration'] #if "duration" in loaded_suggested_data else 0#update the values
          pump_history_1['rate'] = loaded_suggested_data['rate'] #if "rate" in loaded_suggested_data else 0
          pump_history_0['timestamp'] = current_timestamp
          pump_history_1['timestamp'] = current_timestamp

          loaded_pump_history.insert(0, pump_history_1) # insert second element back to whatever we loaded from pumphistory
          loaded_pump_history.insert(0, pump_history_0) #insert first element back to whatever we loaded from pumphistory
          read_pump_history.close()
      
        with open("monitor/pumphistory.json", "w") as write_pump_history:
          json.dump(loaded_pump_history, write_pump_history, indent=4)
    
  ################ Update temp_basal.json with the current temp_basal rate and duration ####################
    
    #load temp_basal.json
    with open("monitor/temp_basal.json") as read_temp_basal:
      loaded_temp_basal = json.load(read_temp_basal)
      loaded_temp_basal['duration']-=5
      
      if loaded_temp_basal['duration']<=0:
        loaded_temp_basal['duration'] = 0
      
      if "doing nothing" not in loaded_suggested_data['reason']:

        if loaded_temp_basal['duration']==0:
          loaded_temp_basal['duration'] = loaded_suggested_data['duration'] #if "duration" in loaded_suggested_data else 0
          loaded_temp_basal['rate'] = loaded_suggested_data['rate'] #if "rate" in loaded_suggested_data else 0


          ######################### Update input of glucosym based on new temp ##############
          # if (loaded_suggested_data['rate'] == 0) and (loaded_suggested_data['duration'] == 0):
          #   loaded_algo_input_copy["events"]['basal'][0]['amt'] = loaded_suggested_data['basal']
          #   loaded_algo_input_copy["events"]['basal'][0]['length'] = 30
          #   loaded_algo_input_copy["events"]['basal'][0]['start'] = _*5
          # else:
            
          #   loaded_algo_input_copy["events"]['basal'][0]['amt'] = loaded_suggested_data['rate'] #if "rate" in loaded_suggested_data else 0
          #   loaded_algo_input_copy["events"]['basal'][0]['length'] = loaded_suggested_data['duration'] #if "duration" in loaded_suggested_data else 0
          #   loaded_algo_input_copy["events"]['basal'][0]['start'] = _*5
          
          ##################### Uppdate Pupmphistory ####################################
            
          with open("monitor/pumphistory.json") as read_pump_history:
            loaded_pump_history = json.load(read_pump_history) # read whole pump_history.json
            pump_history_0 = loaded_pump_history[0].copy()  #load first element
            pump_history_1 = loaded_pump_history[1].copy() #load second element, fist and second are both for one temp basal
            pump_history_0['duration (min)'] = loaded_suggested_data['duration'] #if "duration" in loaded_suggested_data else 0# Activate for non_faulty system
            pump_history_1['rate'] = loaded_suggested_data['rate'] #if "rate" in loaded_suggested_data else 0# Activate for non_faulty System
            pump_history_0['timestamp'] = current_timestamp
            pump_history_1['timestamp'] = current_timestamp

            loaded_pump_history.insert(0, pump_history_1) # insert second element back to whatever we loaded from pumphistory
            loaded_pump_history.insert(0, pump_history_0) #insert first element back to whatever we loaded from pumphistory
            read_pump_history.close()
        
          with open("monitor/pumphistory.json", "w") as write_pump_history:
            json.dump(loaded_pump_history, write_pump_history, indent=4)
          
        
        else:  
          suggested_data_rate = loaded_suggested_data['rate'] #if "rate" in loaded_suggested_data else 0
          if loaded_temp_basal['rate']!=suggested_data_rate:
            loaded_temp_basal['rate']=suggested_data_rate
            loaded_temp_basal['duration']=loaded_suggested_data['duration'] #if "duration" in loaded_suggested_data else 0

            ####################### Update input of glucosym based on new temp ###########
            
            # loaded_algo_input_copy["events"]['basal'][0]['amt'] = loaded_suggested_data['rate'] #if "rate" in loaded_suggested_data else 0
            # loaded_algo_input_copy["events"]['basal'][0]['length'] = loaded_suggested_data['duration'] #if "duration" in loaded_suggested_data else 0
            # loaded_algo_input_copy["events"]['basal'][0]['start'] = _*5

            #################### Uppdate Pumphistory ############################
            
            with open("monitor/pumphistory.json") as read_pump_history:
              loaded_pump_history = json.load(read_pump_history)
              pump_history_0 = loaded_pump_history[0].copy()
              pump_history_1 = loaded_pump_history[1].copy()
              pump_history_0['duration (min)'] = loaded_suggested_data['duration'] #if "duration" in loaded_suggested_data else 0
              pump_history_1['rate'] = loaded_suggested_data['rate'] #if "rate" in loaded_suggested_data else 0
              pump_history_0['timestamp'] = current_timestamp
              pump_history_1['timestamp'] = current_timestamp
              loaded_pump_history.insert(0, pump_history_1)
              loaded_pump_history.insert(0, pump_history_0)
              read_pump_history.close()
          
            with open("monitor/pumphistory.json", "w") as write_pump_history:
              json.dump(loaded_pump_history, write_pump_history, indent=4)
      

  #    else:
  #      if loaded_temp_basal['duration']<=0:
  #        loaded_temp_basal['duration'] = 0
      
      read_temp_basal.close()
    
    ## Fault_injection: Injection of fault in temp_basal ###############################
    
    ##temp_basal:HOOK##

    ############################### End of Fault injection #############################
      
    with open("monitor/temp_basal.json", "w") as write_temp_basal:
      json.dump(loaded_temp_basal, write_temp_basal, indent=4)    
        
    
    #print(suggested_data_to_dump)
    #write the list_suggested_data_to_dump into all_suggested.json file
    #with open("enact/all_suggested.json", "w") as dump_suggested:
    #  json.dump(list_suggested_data_to_dump, dump_suggested, indent=4)
    #  dump_suggested.close()  

    #if 'rate' in loaded_suggested_data.keys():
          #update the insulin parameter input of glucosym. This insulin parameters is received from openaps(suggested.json)
    #  algo_input_list["events"]['basal'][0]['amt'] = loaded_suggested_data['rate']
    #  algo_input_list["events"]['basal'][0]['length'] = loaded_suggested_data['duration']
    #  algo_input_list["events"]['basal'][0]['start'] = _*5
    
    
    
    #os.chdir("../glucosym/closed_loop_algorithm_samples")
    
    ####################### Write algo_input having the suggested output from openaps ##########################
    
    # with open("../glucosym/closed_loop_algorithm_samples/algo_input.json", "w") as write_algo_input:
    #   json.dump(loaded_algo_input_copy, write_algo_input, indent=4)
    
    
    # call(["node", "../glucosym/closed_loop_algorithm_samples/algo_bw.js"]);
  
    
  ##hazardfile.close()

  # print("\n ########################################")
  # print("Fault injected: ", fault_injected)
  # print("Fault Occurrence:", unsafe_action_occurance, " times")
  # print("########################################\n")

  # mse = se / num_data
  # mse_bb = bb_controller_se / num_data
  # with open(f'mse_result/mse_{filename.split(".")[0]}.csv','a') as mse_result:
  #   csv_writer = csv.writer(mse_result)
  #   csv_writer.writerow([current_day, mse, mse_bb, "U"])
  #   mse_result.close()

  # total_mse = total_se / total_num_data
  # bb_controller_total_mse = bb_controller_total_se / total_num_data
  # with open(f'mse_result/mse_{filename.split(".")[0]}.csv','a') as mse_result:
  #   csv_writer = csv.writer(mse_result)
  #   csv_writer.writerow([-1, total_mse, bb_controller_total_mse, "U"])
  #   mse_result.close()

