#!/usr/bin/env bash

python_version=3.9
venv_name=venv

echo "Is 'venv' the folder name of the virtual environment?(Y/n)"
read answer
if [[ "${answer}" == n ]] ; then
  echo "Please enter the folder name of the virtual environment:"
  read venv_name
  while [[ ! -d "./${venv_name}" ]] ; do
    echo "Folder does exist."
    echo "Please enter the folder name of the virtual environment:"
    read venv_name 
  done
fi

#rm -r ./${venv_name}/lib/python${python_version}/site-packages/pip
#rm -r ./${venv_name}/lib/python${python_version}/site-packages/pip-*
#rm -r ./${venv_name}/lib/python${python_version}/site-packages/setuptools
#rm -r ./${venv_name}/lib/python${python_version}/site-packages/setuptools-*
#mv ./dependencies/pip ./${venv_name}/lib/python${python_version}/site-packages
#mv ./dependencies/pip-* ./${venv_name}/lib/python${python_version}/site-packages
#mv ./dependencies/setuptools ./${venv_name}/lib/python${python_version}/site-packages
#mv ./dependencies/setuptools-* ./${venv_name}/lib/python${python_version}/site-packages
#rm -r ./dependencies

pip install numpy==1.21.2 watchdog==2.1.5 nodeenv==1.6.0 openaps==0.1.5 openaps-contrib==0.0.15 matplotlib==3.4.3 sed==0.3.1

#apt-get download python3.9-dev=3.9.10-1+focal1 python3-software-properties=0.99.9.8

#dpkg -x ./python3.9-dev* ./dev
#dpkg -x ./python3-software-properties* ./software-properties

#mv ./dev ./${venv_name}/lib/python${python_version}/site-packages
#mv ./software-properties ./${venv_name}/lib/python${python_version}/site-packages 

#rm ./python3.9-dev*
#rm ./python3-software-properties*

nodeenv -p --node=12.22.1
npm init -g
npm install -g json@11.0.0 oref0@0.7.0

cp -f ./substitution\ files/oref0/basal-set-temp.js ./${venv_name}/lib/node_modules/oref0/lib/
cp -f ./substitution\ files/oref0/determine-basal.js ./${venv_name}/lib/node_modules/oref0/lib/determine-basal/
cp -f ./substitution\ files/oref0/oref0-determine-basal.js ./${venv_name}/lib/node_modules/oref0/bin/

# For python 3 only
cp -f ./substitution\ files/vendors/medtronic.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/vendors/
cp -f ./substitution\ files/decocare/stick.py ./${venv_name}/lib/python${python_version}/site-packages/decocare/
cp -f ./substitution\ files/decocare/session.py ./${venv_name}/lib/python${python_version}/site-packages/decocare/
cp -f ./substitution\ files/decocare/history.py ./${venv_name}/lib/python${python_version}/site-packages/decocare/
cp -f ./substitution\ files/decocare/records/times.py ./${venv_name}/lib/python${python_version}/site-packages/decocare/records/
cp -f ./substitution\ files/decocare/cgm/__init__.py ./${venv_name}/lib/python${python_version}/site-packages/decocare/cgm/
cp -f ./substitution\ files/vendors/process.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/vendors/
cp -f ./substitution\ files/vendors/plugins/add.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/vendors/plugins/
cp -f ./substitution\ files/cli/__init__.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/cli/
cp -f ./substitution\ files/alias/add.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/alias/
cp -f ./substitution\ files/alias/remove.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/alias/
cp -f ./substitution\ files/alias/show.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/alias/
cp -f ./substitution\ files/devices/__init__.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/devices/
cp -f ./substitution\ files/devices/add.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/devices/
cp -f ./substitution\ files/vendors/dexcom.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/vendors/
cp -f ./substitution\ files/dexcom_reader/readdata.py ./${venv_name}/lib/python${python_version}/site-packages/dexcom_reader/
cp -f ./substitution\ files/decocare/fuser.py ./${venv_name}/lib/python${python_version}/site-packages/decocare/
cp -f ./substitution\ files/vendors/plugins/remove.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/vendors/plugins/
cp -f ./substitution\ files/vendors/plugins/show.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/vendors/plugins/
cp -f ./substitution\ files/devices/remove.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/devices/
cp -f ./substitution\ files/devices/show.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/devices/
cp -f ./substitution\ files/config.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/
cp -f ./substitution\ files/builtins.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/
cp -f ./substitution\ files/cli/commandmapapp.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/cli/
cp -f ./substitution\ files/vendors/__init__.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/vendors/
cp -f ./substitution\ files/dexcom_reader/database_records.py ./${venv_name}/lib/python${python_version}/site-packages/dexcom_reader/
cp -f ./substitution\ files/dexcom_reader/util.py ./${venv_name}/lib/python${python_version}/site-packages/dexcom_reader/
cp -f ./substitution\ files/dexcom_reader/packetwriter.py ./${venv_name}/lib/python${python_version}/site-packages/dexcom_reader/
cp -f ./substitution\ files/decocare/commands.py ./${venv_name}/lib/python${python_version}/site-packages/decocare/
cp -f ./substitution\ files/decocare/records/__init__.py ./${venv_name}/lib/python${python_version}/site-packages/decocare/records/
cp -f ./substitution\ files/decocare/records/base.py ./${venv_name}/lib/python${python_version}/site-packages/decocare/records/
cp -f ./substitution\ files/decocare/records/bolus.py ./${venv_name}/lib/python${python_version}/site-packages/decocare/records/
cp -f ./substitution\ files/decocare/link.py ./${venv_name}/lib/python${python_version}/site-packages/decocare/
cp -f ./substitution\ files/vendors/plugins/__init__.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/vendors/plugins/
cp -f ./substitution\ files/uses/__init__.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/uses/
cp -f ./substitution\ files/uses/registry.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/uses/
cp -f ./substitution\ files/reports/__init__.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/reports/
cp -f ./substitution\ files/reports/add.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/reports/
cp -f ./substitution\ files/reports/remove.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/reports/
cp -f ./substitution\ files/reports/invoke.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/reports/
cp -f ./substitution\ files/reports/show.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/reports/
cp -f ./substitution\ files/alias/__init__.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/alias/
cp -f ./substitution\ files/reports/reporters/__init__.py ./${venv_name}/lib/python${python_version}/site-packages/openaps/reports/reporters/
sed -i "1s|.*|#!${PWD}/${venv_name}/bin/python|" ./substitution\ files/openaps
sed -i "1s|.*|#!${PWD}/${venv_name}/bin/python|" ./substitution\ files/openaps-report
cp -f ./substitution\ files/openaps-report ./${venv_name}/bin/
cp -f ./substitution\ files/openaps ./${venv_name}/bin/
# End

cd ./openaps${python_version}
git init

echo "Auto-installation finished!"








