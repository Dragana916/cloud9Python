{"filter":false,"title":"composite-data.py","tooltip":"/composite-data.py","ace":{"folds":[],"scrolltop":272.19140625,"scrollleft":0,"selection":{"start":{"row":30,"column":12},"end":{"row":30,"column":55},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"fe62d934e4d199993e0685efddcdf1413a23a2d2","mime":"text/x-script.python","undoManager":{"mark":47,"position":47,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":11},"action":"insert","lines":["import csv","import copy"],"id":1}],[{"start":{"row":1,"column":11},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":12,"column":1},"action":"insert","lines":["myVehicle = {","    \"vin\" : \"<empty>\",","    \"make\" : \"<empty>\" ,","    \"model\" : \"<empty>\" ,","    \"year\" : 0,","    \"range\" : 0,","    \"topSpeed\" : 0,","    \"zeroSixty\" : 0.0,","    \"mileage\" : 0","}"],"id":3}],[{"start":{"row":12,"column":1},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":38},"action":"insert","lines":["for key, value in myVehicle.items():","    print(\"{} : {}\".format(key,value))"],"id":5}],[{"start":{"row":15,"column":38},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":4},"end":{"row":17,"column":0},"action":"insert","lines":["",""]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "],"id":7}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":20},"action":"insert","lines":["myInventoryList = []"],"id":8}],[{"start":{"row":17,"column":20},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":9},{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["",""]},{"start":{"row":19,"column":0},"end":{"row":20,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":20,"column":0},"end":{"row":40,"column":42},"action":"insert","lines":["with open('car_fleet.csv') as csvFile:","    csvReader = csv.reader(csvFile, delimiter=',')  ","    lineCount = 0  ","    for row in csvReader:","        if lineCount == 0:","            print(f'Column names are: {\", \".join(row)}')  ","            lineCount += 1  ","        else:  ","            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  ","            currentVehicle = copy.deepcopy(myVehicle)  ","            currentVehicle[\"vin\"] = row[0]  ","            currentVehicle[\"make\"] = row[1]  ","            currentVehicle[\"model\"] = row[2]  ","            currentVehicle[\"year\"] = row[3]  ","            currentVehicle[\"range\"] = row[4]  ","            currentVehicle[\"topSpeed\"] = row[5]  ","            currentVehicle[\"zeroSixty\"] = row[6]  ","            currentVehicle[\"mileage\"] = row[7]  ","            myInventoryList.append(currentVehicle)  ","            lineCount += 1  ","    print(f'Processed {lineCount} lines.')"],"id":10}],[{"start":{"row":40,"column":42},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "]},{"start":{"row":41,"column":4},"end":{"row":42,"column":0},"action":"insert","lines":["",""]},{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":42,"column":4},"end":{"row":42,"column":45},"action":"insert","lines":["currentVehicle = copy.deepcopy(myVehicle)"],"id":12}],[{"start":{"row":42,"column":45},"end":{"row":43,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"insert","lines":["    "]},{"start":{"row":43,"column":4},"end":{"row":44,"column":0},"action":"insert","lines":["",""]},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":44,"column":4},"end":{"row":47,"column":22},"action":"insert","lines":["for myCarProperties in myInventoryList:","    for key, value in myCarProperties.items():","        print(\"{} : {}\".format(key,value))","        print(\"-----\")"],"id":14}],[{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"insert","lines":["    "],"id":15},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["    "]},{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":38},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":16},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":4},"end":{"row":17,"column":0},"action":"insert","lines":["",""]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"insert","lines":["p"],"id":17},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":["r"]},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["i"]},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"insert","lines":["n"]},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":17,"column":9},"end":{"row":17,"column":11},"action":"insert","lines":["()"],"id":18}],[{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"insert","lines":["-"],"id":19},{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"insert","lines":["-"]},{"start":{"row":17,"column":12},"end":{"row":17,"column":13},"action":"insert","lines":["-"]},{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"insert","lines":["-"]},{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"insert","lines":["-"]},{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"insert","lines":["-"]},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"insert","lines":["-"]},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"insert","lines":["-"]},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"insert","lines":["-"]},{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"insert","lines":["-"]},{"start":{"row":17,"column":20},"end":{"row":17,"column":21},"action":"insert","lines":["-"]},{"start":{"row":17,"column":21},"end":{"row":17,"column":22},"action":"insert","lines":["-"]},{"start":{"row":17,"column":22},"end":{"row":17,"column":23},"action":"insert","lines":["-"]},{"start":{"row":17,"column":23},"end":{"row":17,"column":24},"action":"insert","lines":["-"]},{"start":{"row":17,"column":24},"end":{"row":17,"column":25},"action":"insert","lines":["-"]},{"start":{"row":17,"column":25},"end":{"row":17,"column":26},"action":"insert","lines":["-"]},{"start":{"row":17,"column":26},"end":{"row":17,"column":27},"action":"insert","lines":["-"]},{"start":{"row":17,"column":27},"end":{"row":17,"column":28},"action":"insert","lines":["-"]},{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"insert","lines":["-"]}],[{"start":{"row":17,"column":29},"end":{"row":17,"column":30},"action":"insert","lines":["-"],"id":20},{"start":{"row":17,"column":30},"end":{"row":17,"column":31},"action":"insert","lines":["-"]},{"start":{"row":17,"column":31},"end":{"row":17,"column":32},"action":"insert","lines":["-"]},{"start":{"row":17,"column":32},"end":{"row":17,"column":33},"action":"insert","lines":["-"]},{"start":{"row":17,"column":33},"end":{"row":17,"column":34},"action":"insert","lines":["-"]},{"start":{"row":17,"column":34},"end":{"row":17,"column":35},"action":"insert","lines":["-"]},{"start":{"row":17,"column":35},"end":{"row":17,"column":36},"action":"insert","lines":["-"]},{"start":{"row":17,"column":36},"end":{"row":17,"column":37},"action":"insert","lines":["-"]},{"start":{"row":17,"column":37},"end":{"row":17,"column":38},"action":"insert","lines":["-"]},{"start":{"row":17,"column":38},"end":{"row":17,"column":39},"action":"insert","lines":["-"]},{"start":{"row":17,"column":39},"end":{"row":17,"column":40},"action":"insert","lines":["-"]},{"start":{"row":17,"column":40},"end":{"row":17,"column":41},"action":"insert","lines":["-"]},{"start":{"row":17,"column":41},"end":{"row":17,"column":42},"action":"insert","lines":["-"]},{"start":{"row":17,"column":42},"end":{"row":17,"column":43},"action":"insert","lines":["-"]},{"start":{"row":17,"column":43},"end":{"row":17,"column":44},"action":"insert","lines":["-"]},{"start":{"row":17,"column":44},"end":{"row":17,"column":45},"action":"insert","lines":["-"]}],[{"start":{"row":42,"column":42},"end":{"row":43,"column":0},"action":"insert","lines":["",""],"id":21},{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"insert","lines":["    "]},{"start":{"row":43,"column":4},"end":{"row":44,"column":0},"action":"insert","lines":["",""]},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]},{"start":{"row":44,"column":4},"end":{"row":45,"column":0},"action":"insert","lines":["",""]},{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"insert","lines":["    "]},{"start":{"row":45,"column":4},"end":{"row":45,"column":5},"action":"insert","lines":["p"]}],[{"start":{"row":45,"column":5},"end":{"row":45,"column":6},"action":"insert","lines":["r"],"id":22},{"start":{"row":45,"column":6},"end":{"row":45,"column":7},"action":"insert","lines":["i"]},{"start":{"row":45,"column":7},"end":{"row":45,"column":8},"action":"insert","lines":["n"]},{"start":{"row":45,"column":8},"end":{"row":45,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":45,"column":9},"end":{"row":45,"column":11},"action":"insert","lines":["()"],"id":23}],[{"start":{"row":45,"column":10},"end":{"row":45,"column":11},"action":"insert","lines":["-"],"id":24},{"start":{"row":45,"column":11},"end":{"row":45,"column":12},"action":"insert","lines":["-"]},{"start":{"row":45,"column":12},"end":{"row":45,"column":13},"action":"insert","lines":["-"]},{"start":{"row":45,"column":13},"end":{"row":45,"column":14},"action":"insert","lines":["-"]},{"start":{"row":45,"column":14},"end":{"row":45,"column":15},"action":"insert","lines":["-"]},{"start":{"row":45,"column":15},"end":{"row":45,"column":16},"action":"insert","lines":["-"]},{"start":{"row":45,"column":16},"end":{"row":45,"column":17},"action":"insert","lines":["-"]},{"start":{"row":45,"column":17},"end":{"row":45,"column":18},"action":"insert","lines":["-"]},{"start":{"row":45,"column":18},"end":{"row":45,"column":19},"action":"insert","lines":["-"]},{"start":{"row":45,"column":19},"end":{"row":45,"column":20},"action":"insert","lines":["-"]},{"start":{"row":45,"column":20},"end":{"row":45,"column":21},"action":"insert","lines":["-"]},{"start":{"row":45,"column":21},"end":{"row":45,"column":22},"action":"insert","lines":["-"]},{"start":{"row":45,"column":22},"end":{"row":45,"column":23},"action":"insert","lines":["-"]},{"start":{"row":45,"column":23},"end":{"row":45,"column":24},"action":"insert","lines":["-"]},{"start":{"row":45,"column":24},"end":{"row":45,"column":25},"action":"insert","lines":["-"]},{"start":{"row":45,"column":25},"end":{"row":45,"column":26},"action":"insert","lines":["-"]},{"start":{"row":45,"column":26},"end":{"row":45,"column":27},"action":"insert","lines":["-"]},{"start":{"row":45,"column":27},"end":{"row":45,"column":28},"action":"insert","lines":["-"]},{"start":{"row":45,"column":28},"end":{"row":45,"column":29},"action":"insert","lines":["-"]},{"start":{"row":45,"column":29},"end":{"row":45,"column":30},"action":"insert","lines":["-"]}],[{"start":{"row":45,"column":30},"end":{"row":45,"column":31},"action":"insert","lines":["-"],"id":25},{"start":{"row":45,"column":31},"end":{"row":45,"column":32},"action":"insert","lines":["-"]},{"start":{"row":45,"column":32},"end":{"row":45,"column":33},"action":"insert","lines":["-"]},{"start":{"row":45,"column":33},"end":{"row":45,"column":34},"action":"insert","lines":["-"]},{"start":{"row":45,"column":34},"end":{"row":45,"column":35},"action":"insert","lines":["-"]},{"start":{"row":45,"column":35},"end":{"row":45,"column":36},"action":"insert","lines":["-"]},{"start":{"row":45,"column":36},"end":{"row":45,"column":37},"action":"insert","lines":["-"]},{"start":{"row":45,"column":37},"end":{"row":45,"column":38},"action":"insert","lines":["-"]},{"start":{"row":45,"column":38},"end":{"row":45,"column":39},"action":"insert","lines":["-"]},{"start":{"row":45,"column":39},"end":{"row":45,"column":40},"action":"insert","lines":["-"]},{"start":{"row":45,"column":40},"end":{"row":45,"column":41},"action":"insert","lines":["-"]},{"start":{"row":45,"column":41},"end":{"row":45,"column":42},"action":"insert","lines":["-"]},{"start":{"row":45,"column":42},"end":{"row":45,"column":43},"action":"insert","lines":["-"]},{"start":{"row":45,"column":43},"end":{"row":45,"column":44},"action":"insert","lines":["-"]},{"start":{"row":45,"column":44},"end":{"row":45,"column":45},"action":"insert","lines":["-"]},{"start":{"row":45,"column":45},"end":{"row":45,"column":46},"action":"insert","lines":["-"]},{"start":{"row":45,"column":46},"end":{"row":45,"column":47},"action":"insert","lines":["-"]},{"start":{"row":45,"column":47},"end":{"row":45,"column":48},"action":"insert","lines":["-"]},{"start":{"row":45,"column":48},"end":{"row":45,"column":49},"action":"insert","lines":["-"]},{"start":{"row":45,"column":49},"end":{"row":45,"column":50},"action":"insert","lines":["-"]},{"start":{"row":45,"column":50},"end":{"row":45,"column":51},"action":"insert","lines":["-"]},{"start":{"row":45,"column":51},"end":{"row":45,"column":52},"action":"insert","lines":["-"]},{"start":{"row":45,"column":52},"end":{"row":45,"column":53},"action":"insert","lines":["-"]},{"start":{"row":45,"column":53},"end":{"row":45,"column":54},"action":"insert","lines":["-"]}],[{"start":{"row":45,"column":54},"end":{"row":45,"column":55},"action":"insert","lines":["-"],"id":26},{"start":{"row":45,"column":55},"end":{"row":45,"column":56},"action":"insert","lines":["-"]},{"start":{"row":45,"column":56},"end":{"row":45,"column":57},"action":"insert","lines":["-"]}],[{"start":{"row":45,"column":4},"end":{"row":45,"column":6},"action":"insert","lines":["# "],"id":27}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":6},"action":"insert","lines":["# "],"id":28}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":6},"action":"remove","lines":["# "],"id":29}],[{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"insert","lines":["\""],"id":30}],[{"start":{"row":17,"column":46},"end":{"row":17,"column":47},"action":"insert","lines":["\""],"id":31}],[{"start":{"row":17,"column":3},"end":{"row":17,"column":48},"action":"remove","lines":[" print(\"-----------------------------------\")"],"id":32}],[{"start":{"row":17,"column":2},"end":{"row":17,"column":3},"action":"remove","lines":[" "],"id":33},{"start":{"row":17,"column":1},"end":{"row":17,"column":2},"action":"remove","lines":[" "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"remove","lines":[" "]},{"start":{"row":16,"column":4},"end":{"row":17,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "],"id":34},{"start":{"row":15,"column":38},"end":{"row":16,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":35}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":45},"action":"insert","lines":[" print(\"-----------------------------------\")"],"id":36}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":1},"action":"remove","lines":[" "],"id":37}],[{"start":{"row":44,"column":3},"end":{"row":44,"column":60},"action":"remove","lines":[" # print(-----------------------------------------------)"],"id":38}],[{"start":{"row":44,"column":2},"end":{"row":44,"column":3},"action":"remove","lines":[" "],"id":39},{"start":{"row":44,"column":1},"end":{"row":44,"column":2},"action":"remove","lines":[" "]},{"start":{"row":44,"column":0},"end":{"row":44,"column":1},"action":"remove","lines":[" "]},{"start":{"row":43,"column":4},"end":{"row":44,"column":0},"action":"remove","lines":["",""]},{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"remove","lines":["    "]},{"start":{"row":42,"column":4},"end":{"row":43,"column":0},"action":"remove","lines":["",""]},{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":41,"column":42},"end":{"row":42,"column":0},"action":"remove","lines":["",""],"id":40}],[{"start":{"row":43,"column":45},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":41},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]},{"start":{"row":44,"column":4},"end":{"row":45,"column":0},"action":"insert","lines":["",""]},{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"insert","lines":["    "]},{"start":{"row":45,"column":4},"end":{"row":46,"column":0},"action":"insert","lines":["",""]},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":46,"column":4},"end":{"row":46,"column":61},"action":"insert","lines":[" # print(-----------------------------------------------)"],"id":42}],[{"start":{"row":46,"column":5},"end":{"row":46,"column":6},"action":"remove","lines":["#"],"id":43}],[{"start":{"row":46,"column":59},"end":{"row":46,"column":61},"action":"insert","lines":["\"\""],"id":44}],[{"start":{"row":46,"column":59},"end":{"row":46,"column":61},"action":"remove","lines":["\"\""],"id":45}],[{"start":{"row":46,"column":12},"end":{"row":46,"column":13},"action":"insert","lines":["\""],"id":46}],[{"start":{"row":46,"column":60},"end":{"row":46,"column":61},"action":"insert","lines":["\""],"id":47}],[{"start":{"row":46,"column":5},"end":{"row":46,"column":6},"action":"remove","lines":[" "],"id":48},{"start":{"row":46,"column":4},"end":{"row":46,"column":5},"action":"remove","lines":[" "]}]]},"timestamp":1680610862107}