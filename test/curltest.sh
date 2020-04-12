#!/bin/bash
let FOUND=0
let KILL=9

#NOTE, because of IDs must be run after the unittesting, so that the database is empty and increment ID is reset

#node ./app.js &
#last_pid=$!
#sleep 2
rm -Rf actual.txt

#TEST1 check hello
curl --silent -k -X GET "https://cs47832.fulgentcorp.com:12137/hello" > actual.txt
if grep "\[{\"message\":\"hello yourself\"}\]" actual.txt; then
    let FOUND=1
else
    let FOUND=0
fi
if [ $FOUND = 0 ]; then
    echo "CURL TEST ERROR: get hello failed"
    #kill -KILL $last_pid
    exit 1
fi

#TEST2 check post
curl --silent -k -X POST "https://cs47832.fulgentcorp.com:12137/properties" \
--header 'x-api-key: cs4783FTW' \
--data-raw '{"address": "123 Test ave", "city": "New York", "state": "NY", "zip": "899999"}' > actual.txt
if grep "\[{\"message\":\"added\"}\]" actual.txt; then
    let FOUND=1
else
    let FOUND=0
fi
if [ $FOUND = 0 ]; then
    echo "CURL TEST ERROR: post properties failed"
    #kill -KILL $last_pid
    exit 1
fi

#TEST3 check get list
curl --silent -k -X GET "https://cs47832.fulgentcorp.com:12137/properties" > actual.txt
OLDESTRECORD=`grep -oP '^[^0-9]*\K[0-9]+' actual.txt` #store the id of the oldest record
if grep "\[{\"ID\"" actual.txt; then
    let FOUND=1
else
    let FOUND=0
fi
if [ $FOUND = 0 ]; then
    echo "CURL TEST ERROR: get properties list failed or empty"
    #kill -KILL $last_pid
    exit 1
fi

#TEST4 check put with all values
curl --silent -k -X PUT "https://cs47832.fulgentcorp.com:12137/properties/1" \
--header 'x-api-key: cs4783FTW' \
--data-raw '{"address": "123 Test ave", "city": "New York", "state": "NY", "zip": "899999"}' > actual.txt
if grep "\[{\"message\":\"updated\"}\]" actual.txt; then
    let FOUND=1
else
    let FOUND=0
fi
if [ $FOUND = 0 ]; then
    echo "CURL TEST ERROR: put properties 1 failed"
    #kill -KILL $last_pid
    exit 1
fi

#TEST5 get the previously updated property
curl --silent -k -X GET "https://cs47832.fulgentcorp.com:12137/properties/1" > actual.txt
if grep "\[{\"ID\":1,\"address\":\"123 Test ave\",\"city\":\"New York\",\"state\":\"NY\",\"zip\":\"899999\"}\]" actual.txt; then
    let FOUND=1
else
    let FOUND=0
fi
if [ $FOUND = 0 ]; then
    echo "CURL TEST ERROR: get properties 1 failed"
    #kill -KILL $last_pid
    exit 1
fi

#TEST6 put attempt without key header test
curl --silent -k -X PUT "https://cs47832.fulgentcorp.com:12137/properties/1" \
--data-raw '{"address": "123 Not Gonna Work", "city": "New York", "state": "NY", "zip": "999999"}' >actual.txt
if grep "{\"message\":\"ERROR: Unauthorized\"}" actual.txt; then
    let FOUND=1
else
    let FOUND=0
fi
if [ $FOUND = 0 ]; then
    echo "CURL TEST ERROR: put properties 1 w/o key failed to return expected error message"
    #kill -KILL $last_pid
    exit 1
fi

#TEST7 put attempt only updating one field
curl --silent -k -X PUT "https://cs47832.fulgentcorp.com:12137/properties/1" \
--header 'x-api-key: cs4783FTW' \
--data-raw '{"address": "123 Updated Version"}' >actual.txt
if grep "\[{\"message\":\"updated\"}\]" actual.txt; then
    let FOUND=1
else
    let FOUND=0
fi
if [ $FOUND = 0 ]; then
    echo "CURL TEST ERROR: put properties 1 update only one field"
    #kill -KILL $last_pid
    exit 1
fi

#TEST8 unauthorized delete
curl --silent -k -X POST "https://cs47832.fulgentcorp.com:12137/properties" \
--header 'x-api-key: cs4783FTW' \
--data-raw '{"address": "123 Test ave", "city": "New York", "state": "NY", "zip": "899999"}'
curl --silent -k -X DELETE "https://cs47832.fulgentcorp.com:12137/properties/2" >actual.txt
if grep "{\"message\":\"ERROR: Unauthorized\"}" actual.txt; then
    let FOUND=1
else
    let FOUND=0
fi
if [ $FOUND = 0 ]; then
    echo "CURL TEST ERROR: Delete properties 2 Unauthorized"
    #kill -KILL $last_pid
    exit 1
fi

#TEST9 try to delete an existing property, authorized
echo $OLDESTRECORD
curl --silent -k -X DELETE "https://cs47832.fulgentcorp.com:12137/properties/$OLDESTRECORD" \
--header 'x-api-key: cs4783FTW' > actual.txt
if grep "\[{\"message\":\"deleted\"}\]" actual.txt; then
    let FOUND=1
else
    let FOUND=0
fi
if [ $FOUND = 0 ]; then
    echo "CURL TEST ERROR: Delete property $OLDESTRECORD"
    #kill -KILL $last_pid
    exit 1
fi

#TEST10 provide non int ID
curl --silent -k -X GET "https://cs47832.fulgentcorp.com:12137/properties/one" > actual.txt
if grep "\[{\"message\":\"ID is not an integer\"}\]" actual.txt; then
    let FOUND=1
else
    let FOUND=0
fi
if [ $FOUND = 0 ]; then
    echo "CURL TEST ERROR: get properties non-int ID"
    #kill -KILL $last_pid
    exit 1
fi


echo "ALL CURL TESTS SUCCESSFUL"
#kill -KILL $last_pid
exit 0
