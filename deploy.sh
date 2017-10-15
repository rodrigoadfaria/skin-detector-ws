#!/bin/bash
cp 'deploy.py' './media/deploy.py'
cd './media/'
python deploy.py
rm 'deploy.py'
cd '..'