#include <pybind11/pybind11.h>
#include "actuator.hpp"

PYBIND11_MODULE(actuator_bindings, m){

    pybind11::class_<Fan>(m, "Fan")
        .def(pybind11::init<>())
        .def("startFan", &Fan::startFan)
        .def("stopFan", &Fan::stopFan);

    pybind11::class_<Humidifier>(m, "Humidifier")
        .def(pybind11::init<>())
        .def("turnHumidifierOn", &Humidifier::turnHumidifierOn)
        .def("turnHumidifierOff", &Humidifier::turnHumidifierOff);

    pybind11::class_<Light>(m, "Light")
        .def(pybind11::init<>())
        .def("turnLightOn", &Light::turnLightOn)
        .def("turnLightOff", &Light::turnLightOff);
}