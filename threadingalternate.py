import variables
import random
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
import matplotlib
import time 
import multiprocessing

totalCasesFinal = [[2000]]
totalCases = [0]
namesList = variables.names
background = variables.background
personList = []
lockdown = [False, 0]
if __name__ == "__main__":
  allSuccesses = []
#there was probably an easier way to do this, but the only language I knew was HTML until the week before starting this project. And I had 9 days to do it unless I wanted to fail my science research class. pain. 
class person:
  def __init__(self, name='NameNotSet', age=0):
        self.name = name
        self.age = age
        self.location = []
        self.moveNum = 0
        self.schedule = []
        self.scheduleFinal = []
        self.movePath = []
        self.infectedBy = []
        self.infectedIn = []
        self.infected = False
        self.infectedType = [0]
        self.infectedTypeNum = 0
        self.lockeddown = False
        self.lockdowndays = 0
        self.immune = False
        self.bathroomCount = 0
        self.infectedOdds = self.infectedType[self.infectedTypeNum]
        self.vaccine = 0
        self.cohort = 0
        self.recentContacts = []
  def move(self):
    originalLocation = self.location
    self.location = self.movePath[self.moveNum]
    if self.scheduleFinal[self.moveNum] == "c":
      background[self.location[0][0]][self.location[0][1]].contains.append([self.name,self.location[1]])
    if self.scheduleFinal[self.moveNum] == "b":
      background[self.location[0][0]][self.location[0][1]].contains.append([self.name,self.location[1]])
    if self.scheduleFinal[self.moveNum] == "li":
      background[self.location[0][0]][self.location[0][1]].contains.append([self.name,self.location[1]])
    if self.scheduleFinal[self.moveNum] == "g":
      background[self.location[0][0]][self.location[0][1]].contains.append([self.name,self.location[1]])
    if self.scheduleFinal[self.moveNum] == "lu":
      background[self.location[0][0]][self.location[0][1]].contains.append([self.name,self.location[1]])
    self.moveNum = self.moveNum + 1
    if self.moveNum > 26:
      self.moveNum = 0
  def infectedProgression(self):
    if self.infectedTypeNum + 1 >= len(self.infectedType):
      self.infectedTypeNum = 0
      self.infectedOdds = self.infectedType[self.infectedTypeNum]
      if len(self.infectedType) != 1:
        self.infected = False
        self.immune = True
        self.infectedType = [0]
    else:
      self.infectedTypeNum += 1
      self.infectedOdds = self.infectedType[self.infectedTypeNum]


def bob(i):
  final = []
  num = random.randint(0,99)
  infectivePeriodTemp = np.random.normal(650,116,1)/100
  infectivePeriod = round(infectivePeriodTemp[0])
  latentPeriodTemp = np.random.normal(8,2,1)
  latentPeriod = round(latentPeriodTemp[0])
  base = [1.02, 1.18, 1.30, 1.34, 1.33, 1.27, 1.19, 1.11, 1.05, 1.01, .99, .98, .99, .99]
  if num > 32:
    num2 = random.randint(0,99)
    if num2 > 80:
      for i23 in range(latentPeriod):
        if i23 >= latentPeriod - 3:
          final.append(1)
        else:
          final.append(0)
      for i24 in range(infectivePeriod):
        if i24 == 0:
          final.append(4.5)
        else:
          final.append(0)
      i288 = 0
      for i67 in range(len(final)):
        if final[i67] == 1:
          for i68 in range(i67, len(final)-1):
            try:
              final[i68] = final[i68] * base[i288]
            except Exception:
              pass
            i288 += 1
          i288 = 0 
          break
    else:
      for i23 in range(latentPeriod):
        if i23 >= latentPeriod - 3:
          final.append(1)
        else:
          final.append(0)
      for i24 in range(infectivePeriod):
          final.append(3.7)
      i288 = 0
      for i67 in range(len(final)):
        if final[i67] == 1:
          for i68 in range(i67, len(final)-1):
            try:
              final[i68] = final[i68] * base[i288]
            except Exception:
              pass
            i288 += 1
          i288 = 0 
          break
  else:
    for i23 in range(latentPeriod):
      if i23 >= latentPeriod - 3:
        final.append(1)
      else:
        final.append(0)
    for i24 in range(infectivePeriod):
        final.append(1)
    i288 = 0
    for i67 in range(len(final)):
      if final[i67] == 1:
        for i68 in range(i67, len(final)-1):
          try:
            final[i68] = final[i68] * base[i288]
          except Exception:
            pass
          i288 += 1
        i288 = 0 
        break
  final2 = []
  for i55 in final:
    for i56 in range(27):
      final2.append(i55)
  personList[i].infectedType = final2




class classroom():
  classroomList = []
  def __init__(self,x,z):
    self.inside = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    self.location = [x,z]
    self.contains = []
    self.count_contains = len(self.contains)
    self.classSize = {} 
  def classSizeOriginalSet(self):
    final = {}
    for i in range(27):
      tempList = []
      for i2 in self.inside:
        tempList.append(0)
      final[i] = tempList
    return final
class bathroom():
  bathroomList = []
  def __init__(self,x,z):
    self.inside = [0,1,2,3]
    self.location = [x,z]
    self.contains = []
    self.count_contains = len(self.contains) 
    self.classSize = {}
  def classSizeOriginalSet(self):
    final = {}
    for i in range(27):
      tempList = []
      for i2 in self.inside:
        tempList.append(0)
      final[i] = tempList
    return final
class gym():
  gymList = []
  def __init__(self,x,z):
    self.inside = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64]
    self.location = [x,z]
    self.contains = []
    self.count_contains = len(self.contains) 
    self.classSize = {}
  def classSizeOriginalSet(self):
    final = {}
    for i in range(27):
      tempList = []
      for i2 in self.inside:
        tempList.append(0)
      final[i] = tempList
    return final
class lunch():
  lunchList = []
  def __init__(self,x,z):
    self.inside = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89]
    self.location = [x,z]
    self.contains = []
    self.count_contains = len(self.contains) 
    self.classSize = {}
  def classSizeOriginalSet(self):
    final = {}
    for i in range(27):
      tempList = []
      for i2 in self.inside:
        tempList.append(0)
      final[i] = tempList
    return final  
class library():
  libraryList = []
  def __init__(self,x,z):
    self.inside = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
    self.location = [x,z]
    self.contains = []
    self.count_contains = len(self.contains) 
    self.classSize = {}
    #format: {period number: [{location 1-14: amount in location at period}]}
  def classSizeOriginalSet(self):
    final = {}
    for i in range(27):
      tempList = []
      for i2 in self.inside:
        tempList.append(0)
      final[i] = tempList
    return final


def checkInfected(period, maskNum):
  vaxx = 0
  for i in range(len(background)):
    for i2 in range(len(background[i])):
      contains = background[i][i2].contains
      if len(contains) > 1:
        for item in contains:
          for item2 in contains:
            if lockdown[0] == False:
              if item[1] == item2[1] and item[0] != item2[0]:
                if personList[item[0]].infected == True or personList[item2[0]].infected == True:
                  if personList[item[0]].cohort == personList[item2[0]].cohort:
                    infect(item, item2, maskNum)
                  #end of infectivity
                  if personList[item2[0]].infectedBy == []:
                    personList[item2[0]].infectedBy = [personList[item[0]].name,[i,i2]]
                  if personList[item[0]].infectedBy == []:
                    personList[item[0]].infectedBy = [personList[item2[0]].name,[i,i2]]
      containsAdd(contains)
      background[i][i2].contains = []

def containsAdd(contains):
  for i in contains:
    addList = []
    for i2 in contains:
      if i[0] != i2[0] and i[1] == i2[1]:
        addList.append(i2[0])
    personList[i[0]].recentContacts.append(addList)

def contactTrace(name, traceTime, period): #Function traces contacts given a name, the current period(period*days), and the time in the past to trace(days)
  traceList = []
  for i in range((traceTime*27)+1):
    if i > period or i == 0:
      continue
    try:
      traceList.append(personList[name].recentContacts[period - i])
    except IndexError:
      print(period)
      print(i)
      print("|")
  return traceList

def contactLockdown(effectivity,name,traceTime,period): #effectivity is decimal
  traceList = contactTrace(name,traceTime,period)
  traced = []
  for i in traceList:
    for i2 in i:
      num = random.randint(0,999)/1000
      if num < effectivity:
        traced.append(i2)
  for i3 in traced:
    if personList[i3].lockeddown == False:
      personList[i3].lockeddown = True
      personList[i3].lockdowndays = 378


def infect(item, item2, maskNum):
  infected = (random.randint(0,99999) / 1000)
  if personList[item[0]].infected == True and personList[item2[0]].immune == False and personList[item2[0]].infected == False and personList[item[0]].lockeddown == False and personList[item2[0]].lockeddown == False:
    vaxx1 = personList[item[0]].vaccine
    vaxx2 = personList[item2[0]].vaccine
    if infected < (personList[item[0]].infectedOdds * (1-maskNum) * (1-vaxx1) * (1-vaxx2)):
      personList[item2[0]].infected = True
      bob(item2[0])
      totalCases[0] = totalCases[0] + 1
  if personList[item2[0]].infected == True and personList[item[0]].immune == False and personList[item[0]].infected == False and personList[item[0]].lockeddown == False and personList[item2[0]].lockeddown == False:
    vaxx1 = personList[item[0]].vaccine
    vaxx2 = personList[item2[0]].vaccine
    if infected < (personList[item2[0]].infectedOdds * (1-maskNum) * (1-vaxx1) * (1-vaxx2)):
      personList[item[0]].infected = True
      bob(item[0])
      totalCases[0] = totalCases[0] + 1

def personMaker():
    for i in range(len(namesList)):
        personList.append(i)
        personList[i] = person()
        personList[i].name = i
        personList[i].age = 18

def backgroundGenerator():
  for i in range(len(background)):
    for i2 in range(len(background[i])):
      if background[i][i2] == "c":
        background[i][i2] = classroom(i,i2)
        classroom.classroomList.append([i,i2])
        background[i][i2].classSize = background[i][i2].classSizeOriginalSet()
      if background[i][i2] == "b":
        background[i][i2] = bathroom(i,i2)
        bathroom.bathroomList.append([i,i2])
        background[i][i2].classSize = background[i][i2].classSizeOriginalSet()
      if background[i][i2] == "g":
        background[i][i2] = gym(i,i2)
        gym.gymList.append([i,i2])
        background[i][i2].classSize = background[i][i2].classSizeOriginalSet()
      if background[i][i2] == "lu":
        background[i][i2] = lunch(i,i2)
        lunch.lunchList.append([i,i2])
        background[i][i2].classSize = background[i][i2].classSizeOriginalSet()
      if background[i][i2] == "li":
        background[i][i2] = library(i,i2)
        library.libraryList.append([i,i2])
        background[i][i2].classSize = background[i][i2].classSizeOriginalSet()

def gymTestingLockdown(run): #run is either true or false, decides if func runs
  if run  == False:
    return 0
  for i in gym.gymList:
    for i2 in background[i[0]][i[1]].contains:
      num = random.randint(0,99)
      if personList[i2[0]].infected == True:
        if personList[i2[0]].lockeddown == False:
          if num < 95:
            personList[i2[0]].lockeddown = True
            personList[i2[0]].lockdowndays = 405 #in periods
      if personList[i2[0]].infected == False:
        if personList[i2[0]].lockeddown == False:
          if num > 94:
            personList[i2[0]].lockeddown = True
            personList[i2[0]].lockdowndays = 405 #in periods
           
def indivLockdown():
  for i in range(len(personList)):
    if personList[i].lockeddown == True:
      if personList[i].lockdowndays > 0:
        personList[i].lockdowndays = personList[i].lockdowndays - 1
      else:
        personList[i].lockeddown = False

 #amount of people tested per day
def surveillanceSelector(testAmount): #start at 5% per day\
  templist = []
  templist = random.sample(personList,testAmount)
  testlist = []
  for i in templist:
      testlist.append(i.name)
  return testlist


positiveDict = []
for i in range(1000):
  positiveDict.append(0)

def testCovid(delayTime, positivityRate, testAmount):
    testlist = surveillanceSelector(testAmount)
    positivePeople = []
    positives = 0
    for i in testlist:
        if personList[i].infected == True:
            num = random.randint(0,99)
            if num < 100: #pcr error rate, 100 is 100% accuracy
                positives += 1
                positivePeople.append(i)
        if personList[i].infected == False:
            num = random.randint(0,99)
            if num > 100: #pcr false positive rate, 100 is 0% false positive chance
                positives += 1
                positivePeople.append(i)
    positiveDict[delayTime] = positives
    if delayTime == 0:
      return [testCheck(positives, positivityRate, testAmount), positivePeople]
    else:
      result = testCheck(positiveDict[0], positivityRate, testAmount)
      max = delayTime
      for i in range(max):
        try:
          holder = positiveDict[i+1]
          positiveDict[i] = holder
        except Exception:
          positiveDict[delayTime] = 0
      return [result, positivePeople]

def testCheck(positives, positivityRate, testAmount):
    if positives/testAmount > positivityRate: #test positivity rate
        return True
    else:
        return False

def testCovidContact(act,delayTime,period,effectivity,traceTime, positivityRate, testAmount): #end of day testing with contact tracing
  if act == False:
    return 0
  positives = testCovid(delayTime, positivityRate, testAmount)[1]
  if len(positives) > 0:
    for i in positives:
      contactLockdown(effectivity,i,traceTime,period)
      if personList[i].lockeddown == False: #contact tracing with infectivity of 2 will still cause all positive tests to self-lockdown
        personList[i].lockeddown = True
        personList[i].lockdowndays = 378 #15 day lockdown (15*27)
    

def checkLockdown(testDelay, positivityRate, testAmount): #lockdowns
  if positivityRate == 0:
    return 0
  if lockdown[0] == False:
    if testCovid(testDelay, positivityRate, testAmount)[0] == True:
      lockdown[0] = True
  else:
    if lockdown[1] == 14:
      lockdown[1] = 0
      lockdown[0] = False
    else:
      lockdown[1] = lockdown[1] + 1

def scheduleDefiner(): #length of schedule is 27, each class takes up 3 slots, 15 minutes long for each slot
#must have 5-7 classes, 1 a lunch, 1-2 free period (gym or library), and 2 bathroom breaks
  periods = 0
  while periods < 9 or periods > 9:
    classnum = random.randint(5,8)
    lunch = 1
    free = random.randint(0,3)
    bathroom = random.randint(2,4)
    periods = classnum + lunch + free
  classes = []
  classes.append(classnum*"c")
  classes.append(free*"f")
  classes.append(lunch*"l")
  classes.append(bathroom*"b")
  return classes

def scheduleMaker():
  for i in range(len(personList)):
    schedule = []
    scheduleTemplate = scheduleDefiner()
    classcount = len(scheduleTemplate[0])
    freecount = len(scheduleTemplate[1])
    lunchcount = len(scheduleTemplate[2])
    personList[i].bathroomCount = len(scheduleTemplate[3])
    while classcount != 0 or freecount != 0 or lunchcount != 0:
      num = random.randint(0,2)
      if num == 0 and classcount != 0:
        schedule.append("c")
        classcount = classcount - 1
      if num == 1 and freecount != 0:
        schedule.append("f")
        freecount = freecount - 1
      if num == 2 and lunchcount != 0:
        schedule.append("lu")
        lunchcount = lunchcount - 1
    personList[i].schedule = schedule
  for i8 in range(len(personList)):
    finalSchedule = []
    schedule2 = []
    counter = 0
    for item in personList[i8].schedule:
      if item == "c":
        seatNum = random.randint(0,19)
        classNum = random.randint(0,len(classroom.classroomList)-1)
        for i3 in range(3):
          if personList[i8].bathroomCount == 0:
            finalSchedule.append([classroom.classroomList[classNum], seatNum])
            schedule2.append("c")
            background[classroom.classroomList[classNum][0]][classroom.classroomList[classNum][1]].classSize[counter][seatNum] += 1
            counter = counter + 1
          if personList[i8].bathroomCount != 0:
            num = random.randint(1,2)
            personList[i8].bathroomCount = personList[i8].bathroomCount - 1
            if num == 2:
              bathNum = random.randint(0,len(bathroom.bathroomList)-1)
              placeNum = random.randint(0,3)
              finalSchedule.append([bathroom.bathroomList[bathNum],placeNum])
              schedule2.append("b")
              background[bathroom.bathroomList[bathNum][0]][bathroom.bathroomList[bathNum][1]].classSize[counter][placeNum] += 1
              counter = counter + 1
            else:
              finalSchedule.append([classroom.classroomList[classNum], seatNum])
              schedule2.append("c")
              background[classroom.classroomList[classNum][0]][classroom.classroomList[classNum][1]].classSize[counter][seatNum] += 1
              counter = counter + 1
      if item == "f":
        decideNum = random.randint(1,2)
        if decideNum == 1:
          placeNum = random.randint(0,49)
          for i4 in range(3):
            finalSchedule.append([library.libraryList[0], placeNum])
            background[library.libraryList[0][0]][library.libraryList[0][1]].classSize[counter][placeNum] += 1
            schedule2.append("li")
            counter = counter + 1
        else:
          placeNum = random.randint(0,64)
          locNum = random.randint(0,len(gym.gymList)-1)
          for i7 in range(3):
            finalSchedule.append([gym.gymList[locNum],placeNum])
            schedule2.append("g")
            background[gym.gymList[locNum][0]][gym.gymList[locNum][1]].classSize[counter][placeNum] += 1
            counter = counter + 1
      if item == "lu":
        placeNum = random.randint(0,89)
        for i5 in range(3):
          finalSchedule.append([lunch.lunchList[0],placeNum])
          schedule2.append("lu")
          background[lunch.lunchList[0][0]][lunch.lunchList[0][1]].classSize[counter][placeNum] += 1
          counter = counter + 1 
    personList[i8].movePath = finalSchedule
    personList[i8].scheduleFinal = schedule2


vaxList = []   
for i in range(1000):
  vaxList.append([0])

def billGates(vaxDelay, vaxAmount): #vaccinate
  selectAmount = vaxAmount
  selectList = []
  for i in range(len(personList)):
    if personList[i].immune == False and personList[i].vaccine == 0:
      selectList.append(personList[i])
  i = 0
  counter = 0
  while i != 10:
    try:
      tempList = random.sample(selectList,selectAmount)
    except ValueError:
      tempList = selectList
    i = 10
    for i2 in tempList:
      if i2.vaccine != 0:
        i += 1
    counter+= 1
    if counter > 49:
      break
  vaxList[vaxDelay] = tempList
  if vaxDelay == 0:
    for i3 in tempList:
      i3.vaccine = .95 #effectiveness of vaccine
  else:
    for i5 in vaxList[0]:
      if vaxList[0] != [0]:
        i5.vaccine = .95
    max = vaxDelay
    for i in range(max):
      try:
        holder = vaxList[i+1]
        vaxList[i] = holder
      except Exception:
        vaxList[vaxDelay] = 0

def assignCohort(cohortNum):
  i = 0
  while i < len(personList):
    for i2 in range(cohortNum):
        cohortMaker(i2, personList[i].name)
        i = i+1
def cohortMaker(i, person1):
  personList[person1].cohort = i
  
def dayTesting(act, accuracy, lockdown): #decimal
  if act == False:
    return 0
  for i in range(len(personList)):
    num = random.randint(0,999)/1000 
    if personList[i].infected == True and personList[i].lockeddown == False:
      if num < accuracy:
        if lockdown == True:
          personList[i].lockeddown = True
          personList[i].lockdowndays = 378
        else:
          personList[i].lockeddown = True
          personList[i].lockdowndays = 27

      


def test():
  finalTest = []
  for i in range(len(personList)):
    testList = []
    for i2 in range(len(personList[i].scheduleFinal)):
      if personList[i].scheduleFinal[i2] == "c":
        if personList[i].movePath[i2][0] in classroom.classroomList:
          testList.append(True)
        else:
          testList.append(False)
      if personList[i].scheduleFinal[i2] == "b":
        if personList[i].movePath[i2][0] in bathroom.bathroomList:
          testList.append(True)
        else:
          testList.append(False)
      if personList[i].scheduleFinal[i2] == "li":
        if personList[i].movePath[i2][0] in library.libraryList:
          testList.append(True)
        else:
          testList.append(False)
      if personList[i].scheduleFinal[i2] == "lu":
        if personList[i].movePath[i2][0] in lunch.lunchList:
          testList.append(True)
        else:
          testList.append(False)
      if personList[i].scheduleFinal[i2] == "g":
        if personList[i].movePath[i2][0] in gym.gymList:
          testList.append(True)
        else:
          testList.append(False)        
    finalTest.append(testList)
  return finalTest

def startVax(amount):
  tempList = random.sample(range(0,1500),amount)
  for i in tempList:
    personList[i].vaccine = .95
def testLockdown():
  num = 0
  for i in range(len(personList)):
    if personList[i].lockeddown == True:
      num += 1
  return num
def selectStartingInfected(num):
  for i in personList:
    i.infected = False
  for i in range(num):
    infNum = True
    vax = 0
    while infNum == True and vax == 0:
      choose = random.randint(0,1499)
      infNum = personList[choose].infected
      vax = personList[choose].vaccine
    personList[choose].infected = True
    
    personList[choose].infectedBy = [0,"start"]
    bob(choose)
def amountInfected():
  counter = 0
  for i in range(len(personList)):
    if personList[i].infected == True:
      counter+=1
  return counter
def amountImmune():
  counter = 0
  for i in range(len(personList)):
    if personList[i].immune == True:
      counter += 1
  return counter
def mover():
  for i in range(len(personList)):
    personList[i].move()
def infectorGrower():
  for i in range(len(personList)):
    personList[i].infectedProgression()
def hardReset(startInfect, cohortNum):
  for i in range(len(personList)):
    personList[i].infected = False
    personList[i].immune = False
    personList[i].lockeddown = False
    personList[i].recentContacts = []
    personList[i].vaccine = 0
    personList[i].lockdowndays = 0
  totalCases[0] = 0
  lockdown[0] = False
  lockdown[1] = 0
  vaxList = []   
  for i in range(1000):
    vaxList.append([0])
  positiveDict = []
  for i in range(1000):
    positiveDict.append(0)
  selectStartingInfected(startInfect)
  assignCohort(cohortNum)
  scheduleMaker()



personMaker()
backgroundGenerator() 
scheduleMaker()
#above three are critical, any other base funcs add after here



#base: MAX=0, DAYS=0, startInfect = 1, cohortNum = 1, maskEffectivity = 0, delayTime = 0, gymTest = False, positivityRate = 0, testAmount = 0, vaxAmount = 0, testNum = varied
def runTest(MAX, DAYS, startInfect, cohortNum, maskEffectivity, vaxdelayTime, gymTest, positivityRate, testAmount, vaxAmount, testNum, lockdelayTime, contactTracingAct, contactTracingEffectivity, contactTracingTraceTime, dayTestingBreakup, dayTestingAct, dayTestingAccuracy, dayTestingLockdown, startVaxAmount):
  filenameTemp = "days-"+ str(DAYS) + " starting infected-" +str(startInfect) + " cohorts-"  + str(cohortNum) +  " mask-"+ str(round(maskEffectivity,4)) + " vdtime-"  + str(vaxdelayTime)+ " lockdtime-" + str(lockdelayTime) + " gymTest-" + str(gymTest) + " prate-" + str(round(positivityRate,4)) + " tamount-" + str(testAmount) + " vamount-" + str(vaxAmount) + " cTracing-" + str(contactTracingAct) + " tTime-" + str(contactTracingTraceTime) + " trEffec-" + str(round(contactTracingEffectivity,2)) + " dTesting-" + str(dayTestingAct) + " acc-" + str(round(dayTestingAccuracy,2)) + " dTLock-" + str(dayTestingLockdown) + " dTBreak-" + str(dayTestingBreakup) + " svAmount-" + str(startVaxAmount)
  filename = filenameTemp.replace(".",",")
  print(filename)
  colors = ["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"]
  colorpicker = 0
  selectStartingInfected(startInfect)
  assignCohort(cohortNum)
  startVax(startVaxAmount)
  finalList1 = []
  rnaughtFinal = []
  counterList = []
  incidence = []
  counterList2 = []
  period = 0
  periods = []
  for i3 in range(MAX): #number of independent runs
    #data creation
    for i43 in range(DAYS): #number of days. Changeable
      if i43 % dayTestingBreakup == 0:
        dayTesting(dayTestingAct, dayTestingAccuracy, dayTestingLockdown) #whether to daytest, accuracy of testing, whether to lock down positives or not (require negative to enter vs test on entry and forcibly lock down)
      for i6 in range(27): #number of periods in a day, do not change (9 periods, broken into 3 15 min blocks)
        mover()
        gymTestingLockdown(gymTest)
        checkInfected(i43, maskEffectivity) #(day, mask effectivity)
        counter3 = 0
        for i in range(len(personList)):
          if personList[i].infected == True:
            counter3 += 1
        counterList.append(counter3)
        periods.append(period)
        period += 1
        indivLockdown()
        infectorGrower()
      checkLockdown(lockdelayTime, positivityRate, testAmount)
      billGates(vaxdelayTime, vaxAmount)
      testCovidContact(contactTracingAct, lockdelayTime,i43*27,contactTracingEffectivity,contactTracingTraceTime, positivityRate, testAmount)
      counterList2.append(counterList[len(counterList)-1])
    rnaughtTemp  = []
    incidTemp = []
    i69 = 0
    while i69 < len(counterList2):
      try:
        happyVariable = counterList2[i69+1] - counterList2[i69]
      except Exception: #yes this is lazy it's 3 am
        pass
      incidTemp.append(happyVariable)
      i69 += 1
    incidence.append(incidTemp)
    i32 = 0
    while i32 < len(counterList2): #rNaught
      try:
        happyVariable = counterList2[i32+1]/counterList2[i32]
        rnaughtTemp.append(happyVariable)
      except Exception:
        rnaughtTemp.append(0)
      i32 += 1
    rnaughtFinal.append(rnaughtTemp)
    counterList2 = []
    totalCasesFinal[0].append(totalCases[0])
    hardReset(startInfect, cohortNum)
    #data processing
    xVal = periods
    yVal = counterList
    plt.plot(xVal, yVal, color = colors[colorpicker])
    colorpicker += 1
    if colorpicker == len(colors):
      colorpicker = 0
    finalList1.append(counterList)
    counterList = []
    print(str(i3/MAX*100) + "% done")
    period = 0
    periods = []
  plt.ylabel("$i_{t}$")
  plt.xlabel("Time")
  plt.savefig(fname=filename)
  plt.close()

  f = open(filename + ".txt","w")

  f.write("\nincidence = ")
  f.write(str(incidence))
  f.write("\nrarray = ")
  f.write(str(rnaughtFinal))
  f.write("\ncases = ")
  f.write(str(finalList1))


  def printIncidence():
    for i in range(len(incidence)):
        for i2 in range(len(incidence[i])):
            plt.scatter(i2,incidence[i][i2], s=2, color="blue")
        print(str(i/len(incidence)*100) + "% done")
    plt.xlabel("Incidence")

  def printrnaught():
    for i in range(len(rnaughtFinal)):
        for i2 in range(len(rnaughtFinal[i])):
            plt.scatter(i2, rnaughtFinal[i][i2], s=2, color="green")
        print(str(i/len(rnaughtFinal)*100) + "% done")
    plt.xlabel("R0")
  def timetopeak(arr1):
    finallist = []
    for i in range(len(arr1)):
        final = [0, 0]
        z = 0
        for i2 in range(len(arr1[i])):
            if final[0] < arr1[i][i2]:
                z = arr1[i][i2]
                final = [i2, z]
        if final[1] > 1:
            finallist.append(final[0]/27)
    return finallist

  def maxpeak(arr1):
    finallist = []
    for i in range(len(arr1)):
        final = 0
        for i2 in range(len(arr1[i])):
            if final < arr1[i][i2]:
                final = arr1[i][i2]
        if final > 1:
            finallist.append(final)
    return finallist


  timePeak353535 = timetopeak(finalList1)
  maxPeak353535 = maxpeak(finalList1)

  timePeakInterval = st.norm.interval(alpha=.95, loc=np.mean(timePeak353535), scale=st.sem(timePeak353535))

  maxPeakInterval = st.norm.interval(alpha=.95, loc=np.mean(maxPeak353535), scale=st.sem(maxPeak353535))
  x1 = np.mean(maxPeak353535)
  x2 = np.mean(timePeak353535)
  st1 = np.std(maxPeak353535)
  st2 = np.std(timePeak353535)

  plt.subplot(1,2,1)
  printIncidence()
  plt.subplot(1,2,2)
  printrnaught()
  plt.xlabel("Time (Days)")

  plt.savefig("incidence r0 " + filename)
  plt.close()


  f2 = open("CI mean stdev " + filename + ".txt","w")
  f2.write("Time to Peak:\n")
  f2.write("Mean: " + str(x2))
  f2.write("\nstdev: "+ str(st2))
  f2.write("\nCI: " + str(timePeakInterval))

  f2.write("\nMax Peak:\n")
  f2.write("Mean: " + str(x1))
  f2.write("\nstdev: "+ str(st1))
  f2.write("\nCI: " + str(maxPeakInterval))

  f3 = open("infected all time " + filename + ".txt","w")
  f3.write(str(totalCasesFinal))
  f3.close()
  successes = 0
  for i12 in totalCasesFinal:
    for i13 in i12:
      if i13 < 200:
        successes += 1
  totalCasesFinal[0] = [2000]
  f8 = open(str(testNum)+ ".txt", "w")
  f8.write(str((successes/MAX)*100))
  f8.close()


#base: MAX=0, DAYS=0, startInfect = 1, cohortNum = 1, maskEffectivity = 0, delayTime = 0, gymTest = False, positivityRate = 0, testAmount = 0, vaxAmount = 0, testNum = varied



if __name__ == "__main__":
    MAX1 = 100 #amount of runs
    DAYS1 = 150 #amount of days
    startInfect = 1 #amount of starting infecteds
    cohortNum = 1 #amount of groups population is split into
    maskEffectivity = .53 #effectivity of masks
    vaxdelayTime = 0 #delay until vaccine protection is enables
    lockdelayTime = 0 #testing delay
    gymTest = False #whether those in the gym should be tested and individually locked down if positive
    testAmount = 25 #amount to be tested for lockdowns and contact tracing
    vaxAmount = 0 #amount to be vaxxed per day
    startVaxAmount = 0 #amount of people to be vaxxed before beginning of outbreak
    positivityRate = .1 #lockdown threshold, only applies to lockdowns
    successList = []
    controlList = []
    labels = []
    #contact tracing
    contactTracingAct = False #whether contact tracing happens or not
    contactTracingEffectivity = 0 #decimal, how effective the contact  tracing is
    contactTracingTraceTime = 5 #in days, how far back the contacts are traced
    #daily testing 
    dayTestingBreakup = 4 #amount of days between tests (test every "x" days)
    dayTestingAct = False #whether to daytest or not
    dayTestingAccuracy = 1 #accuracy of daytesting
    dayTestingLockdown = False #whether to lockdown positives or not
    outsideIterations = 3
    insideIterations = 6
    counter2 = 0
    processList = []
    filename = "Name" #name of successes graph file
    for i in range(outsideIterations):
      testAmount = 20
      for i2 in range(insideIterations):
        p = multiprocessing.Process(target = runTest, args=(MAX1, DAYS1, startInfect, cohortNum, maskEffectivity, vaxdelayTime, gymTest, positivityRate, testAmount, vaxAmount, counter2,lockdelayTime, contactTracingAct, contactTracingEffectivity, contactTracingTraceTime, dayTestingBreakup, dayTestingAct, dayTestingAccuracy, dayTestingLockdown, startVaxAmount))
        p.start()
        processList.append(p)
        labels.append("VX:"+ str(round(vaxAmount, 2)) + "\nSV:" + str(round(startVaxAmount,2)))
        counter2 += 1
        testAmount += 20
        controlList.append(counter2) 
      positivityRate += .1
      #now wait for all to end

if __name__ == "__main__":
  print(processList)
  for item in range(len(processList)):
    processList[item].join()
    print("done")

if __name__ == "__main__":
  for i in range(len(controlList)):
    f9 = open(str(i)+ ".txt", "r")
    lines = f9.readlines()
    for line in lines:
      successList.append(float(line.rstrip()))
    f9.close()
  print(successList)
  matplotlib.rc("xtick", labelsize = 4)
  plt.plot(controlList, successList, marker = "o", color="green")
  plt.ylabel("% successes")
  plt.xlabel("")
  plt.xticks(controlList, labels)
  plt.ylim(0,100)
  plt.savefig("percent successes"+ filename)
  f6 = open("Successes " + filename + ".txt","w")
  f6.write(str(successList))
  f6.close()









