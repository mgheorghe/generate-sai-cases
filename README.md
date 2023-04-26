# generate-sai-cases

```
git clone https://github.com/opencomputeproject/SAI.git



```


## phase 1:
run all tests - results 100% fail

## phase 2:
run all tests on by one

## phase 3:
run only the test cases that have no mandatory attributes

# phase 4:
in cases that require mandatory attributes put proper values for those attributes
identify how to do int, list ,......

phase 5:
run all cases that have mandatory attributes but do not have a parent (depedency on other object)

phase 6:
create depedency graph between SAI objects

phase 7:
run all cases that have depedency on other attributes but those depdencies are on objects from other cases that already passed in phase 1-6
