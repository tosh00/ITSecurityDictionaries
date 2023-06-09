#!/bin/bash

# Output file for storing cookies
output_file="cookies.txt"

rm "$output_file"

# Loop to send n requests
for ((i=1; i<=$1; i++))
do
    # Sending a request to the URL
    response=$(curl -s "http://ubuntu:4400/1" -i)

    # Extracting the "example1-session" cookie from the response
    cookie=$(echo "$response" | grep -oP '(?<=example1-session=)[^;]+')

    # Writing the cookie to the output file
    echo "$cookie" >> "$output_file"
done

echo "Requests completed. Cookies written to $output_file."