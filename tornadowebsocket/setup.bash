#!/usr/bin/env bash

if [ ! -d "${python3_virtualenv_path:=/opt/virtualenvs/tornadowebsocket}" ]
then
  mkdir -p "${python3_virtualenv_path}"
  ${python3_virtualenv:=/usr/local/bin/virtualenv-3.5} -p "${python3_path:=/usr/local/bin/python3.5}" "${python3_virtualenv_path}"
fi

if [[ "${@}" == "install" ]]
then
  "${python3_virtualenv_path}/bin/python" setup.py bdist_egg
  "${python3_virtualenv_path}/bin/easy_install" dist/*.egg
elif [[ "${@}" == "develop" ]]
then
  "${python3_virtualenv_path}/bin/pip" uninstall -y tornadowebsocket
  "${python3_virtualenv_path}/bin/python" setup.py "${@}"
elif [[ "${@}" == "clean" ]]
then
  "${python3_virtualenv_path}/bin/pip" uninstall -y tornadowebsocket
  "${python3_virtualenv_path}/bin/python" setup.py clean
  rm -Rf dist
  rm -Rf build
  rm -Rf *.egg-info
else
  echo "${@}" "should be one of {'install', 'clean', 'develop'}"
fi
