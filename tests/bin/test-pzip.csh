#! /bin/csh -f
set TEST_HOME = ${PWD}/tests
set source_file = pzip.c
set binary_file = pzip
set bin_dir = ${TEST_HOME}/bin
set test_dir = ${TEST_HOME}/tests-pzip
python ${test_dir}/generator.py  100 ${test_dir}/1.in
cp ${test_dir}/1.in ${test_dir}/test.in
${bin_dir}/serialized_runner.py `date +%s` -1 ${bin_dir}/generic-tester.py -s $source_file -b $binary_file -t $test_dir -f="'-pthread -O3'" --timed $argv[*]
