from fastapi import FastAPI
import uvicorn
import pickle

app = FastAPI(debug=True)

@app.get('/')
def home():
    return {'text': 'Car pricing Prediction Solution'}


@app.get('/predict')
def predict(model_key:int, mileage:int,engine_power:int, fuel:int,paint_color: int, car_type: int, private_parking_available:int, has_gps:int,has_air_conditioning: int,automatic_car:int,has_getaround_connect:int,has_speed_regulator:int,winter_tires:int):

 model = pickle.load(open('model.pkl', 'rb'))
 makepredicition = model.predict([[model_key,mileage,engine_power,fuel,paint_color,car_type,private_parking_available,has_gps,has_air_conditioning,automatic_car,has_getaround_connect,has_speed_regulator,winter_tires]])

 output = round(makepredicition[0],2)
 return{'You can sell your car for {}'.format(output)}




if __name__ =='__main__':
    uvicorn.run(app)
