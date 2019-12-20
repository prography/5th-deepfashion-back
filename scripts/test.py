import datetime

file_name = str(datetime.datetime.now().hour) + str(datetime.datetime.now().minute) + ".txt"
output = open("../../opt/python/current/app/scripts/results/" + file_name, "w+")
output.write(str(datetime.datetime.now()))
output.close()
