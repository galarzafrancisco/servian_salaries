#!/bin/bash

date >> logs.log
docker run --rm servian_salaries >> logs.log