#include "actuator.hpp"

Fan::Fan():
    pin(0),
    fanState(false)
{};

void Fan::startFan(){
    fanState = true;
};

void Fan::stopFan(){
    fanState = false;
};

bool Fan::getState() const{
    return fanState;
};


Humidifier::Humidifier():
    pin(1),
    humidifierState(false)
{};

void Humidifier::turnHumidifierOn(){
    humidifierState = true;
};

void Humidifier::turnHumidifierOff(){
    humidifierState = false;
};

bool Humidifier::getState() const{
    return humidifierState;
};


Light::Light():
    pin(2),
    lightState(false)
{};

void Light::turnLightOn(){
    lightState = true;
};

void Light::turnLightOff(){
    lightState = false;
};

bool Light::getState() const{
    return lightState;
};