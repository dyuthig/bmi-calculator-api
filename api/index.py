from flask import Flask

app = Flask(__name__)
import json

with open("boybmi.json") as bmifile:
  global boybmidata
  boybmidata = json.loads(bmifile.read())

with open("girlbmi.json") as bmifile:
  global girlbmidata
  girlbmidata= json.loads(bmifile.read())


def boybmi(age, BMI, months):
  global status
  status = "Blank"
  bmirange = boybmidata[str(age)][0 if months == 0 else 1]
  if BMI < bmirange[0]:
    status = ("Underweight")
  if BMI >= bmirange[0] and BMI < bmirange[1]:
    status = ("Healthy Weight")
  if BMI >= bmirange[1] and BMI < bmirange[2]:
    status = ("Overweight")
  if BMI >= bmirange[2]:
    status = ("Obesity")
  return status


def girlbmi(age, BMI, months):
  global status
  status = "Blank"
  bmirange = girlbmidata[str(age)][0 if months == 0 else 1]
  if BMI < bmirange[0]:
    status = ("Underweight")
  if BMI >= bmirange[0] and BMI < bmirange[1]:
    status = ("Healthy Weight")
  if BMI >= bmirange[1] and BMI < bmirange[2]:
    status = ("Overweight")
  if BMI >= bmirange[2]:
    status = ("Obesity")
  return status


  



def bmi(age, months, totalweight, heightfeet, heightinches, decimalheight, sex):
    validmonths = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    totalheight = heightfeet * 12
    totalheight = totalheight + heightinches + decimalheight
    BMI = totalweight / (totalheight**2) * 703
    BMI = round(BMI, 1)
    months = "N/A"
    if age < 20:
      while True:
        if months not in validmonths:
          return {
              "error": "Month is not valid"
          }
        else:
          break
      if months == 0 or months == 1 or months == 2 or months == 3:
        months = 0
      if months == 4 or months == 5 or months == 6 or months == 7 or months == 8:
        months = 6
      else:
        age = age + 1
        months = 0
      sexlist=["female", "f", "male", "m"]
      
      while True:
        if sex not in sexlist:
          return {
              "error": "Sex is not valid"
          }
        else:
          break   
      if sex == "female".lower() or sex == "f".lower():
        girlbmi(age, BMI, months)
      if sex == "male".lower() or sex== "m".lower():
        boybmi(age, BMI, months)
    elif age >= 20:
      if BMI < 18.5:
        status = ("Underweight")
      elif BMI >= 18.5 and BMI <= 24.9:
        status = ("Healthy Weight")
      elif BMI >= 25.0 and BMI <= 29.9:
        status = ("Overweight")
      elif BMI >= 30.0:
        status = ("Obesity")
    return {
        "status": status,
        "BMI": BMI
    }


@app.route('/<age>/<months>/<totalweight>/<heightfeet>/<heightinches>/<decimalheight>/<sex>')
def home(age,months, totalweight, heightfeet,heightinches,decimalheight,sex):
    return bmi(int(age), int(months), int(totalweight), int(heightfeet),int(heightinches),int(decimalheight),int(sex))
