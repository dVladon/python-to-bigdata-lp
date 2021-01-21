#! /bin/bash

if [[ "${LOCAL_MODE}" = true ]]; then
    echo "=> Executing command '$@'"
    eval $@
else
    echo "=> Skip command '$@' because of non local"
fi
