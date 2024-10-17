#ifndef ACTUATOR_HPP
#define ACTUATOR_HPP

class Fan{
    private:

    public:
    Fan();

    void startFan();
    
    void stopFan();

};

class Humidifier{
    private:
    
    public:
    Humidifier();

    void turnHumidifierOn();
    
    void turnHumidifierOff();
};

class Light{
    private:
    public:
    Light();

    void turnLightOn();

    void turnLightOff();
};

#endif // ACTUATOR_HPP