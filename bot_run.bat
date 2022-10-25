@echo off

call %~dp0NewFVSC\venv\Scripts\activate

cd %~dp0NewFVSC

set TOKEN=5792503942:AAEmiFjQ-6zGXau3AasCFQpztORclXq7kDc

python main.py

pause