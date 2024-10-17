#include <pybind11/pybind11.h>
#include "sensors.hpp"
#include "actuator.hpp"

/**
 * @brief Module voor sensor bindings.
 * 
 * @details Deze module biedt Python bindings voor de SCD4X en VEML6030 sensoren.
 * Hierdoor kunnen deze sensoren gebruikt worden in python.
 */
PYBIND11_MODULE(sensor_bindings, m){
    /**
     * @brief klassebinding van de SCD4X sensor
     * 
     * Dit maakt het mogelijk om de SCD4X sensor te gebruiken en bijvoorbeeld de luchtvochigheidswaarden uit te lezen.
     */
    pybind11::class_<SCD4X>(m, "SCD4X")
        .def(pybind11::init<>())
        .def("readCO2", &SCD4X::readHumidity);

    /**
     * @brief klassebinding van de VEML6030 sensor
     * 
     * Dit maakt het mogelijk om de VEML6030 sensor te gebruiken en bijvoorbeeld licht intensiteit te meten.
     */
    pybind11::class_<VEML6030>(m, "VEML6030")
        .def(pybind11::init<>())
        .def("readLightIntensity", &VEML6030::readLightIntensity);
}

PYBIND11_MODULE(actuator_bindings, m){

    pybind11::class_<Fan>(m, "Fan")
        .def(pybind11::init<>())
        .def("startFan", &Fan::startFan)
        .def("stopFan", &Fan::stopFan);

    pybind11::class_<Humidifier>(m, "Humidifier")
        .def(pybind11::init<>())
        .def("startFan", &Humidifier::turnHumidifierOn)
        .def("stopFan", &Humidifier::turnHumidifierOff);

    pybind11::class_<Light>(m, "Light")
        .def(pybind11::init<>())
        .def("turnLightOn", &Light::turnLightOn)
        .def("turnLightOff", &Light::turnLightOff);
}