#!/bin/bash

source /usr/share/python/fixity/bin/activate
cd /usr/lib/archivematica/fixity

STORAGE_SERVICE_URL=http://amtest4.cern.ch:8000 STORAGE_SERVICE_USER=admin STORAGE_SERVICE_KEY=666f9f2ee9f13fe8eb74e95965ab7c46150a576f REPORT_URL=http://amtest4.cern.ch:8181/ fixity $*

deactivate
