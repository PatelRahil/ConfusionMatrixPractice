import random

print('Confusion Matrix Practice\nBy Rahil Patel')

lower1 = 10
higher1 = 49

lower2 = -5
higher2 = 5



tp = random.randint(lower1, higher1)
fp = random.randint(lower1,higher1)
tn = random.randint(lower1,higher1)
fn = random.randint(lower1,higher1)

costTp = random.randint(lower2, higher2)
costFp = random.randint(lower2, higher2)
costTn = random.randint(lower2, higher2)
costFn = random.randint(lower2, higher2)

print(f'\n\n\nCosts |\n-----------------------\nTrue Positive (TP) = {costTp}\nFalse Positive (FP) = {costFp}\nFalse Negative (FN) = {costFn}\nTrue Negative (TN) = {costTn}')

print('---------------------------------------------')
print('Confusion             |       Outcome       |')
print('   Matrix             | Positive | Negative |')
print('---------------------------------------------')
print(f'           | Positive |    {tp}    |    {fp}    |')
print('Prediction |---------------------------------')
print(f'           | Negative |    {fn}    |    {tn}    |')
print('---------------------------------------------')

expected_value_guess = input('Expected Value = ')
accuracy_guess = input('Accuracy = ')
precision_guess = input('Precision = ')
sensitivity_guess = input('Sensitivity = ')
specificity_guess = input('Specificity = ')

expected_value_actual = costTp*tp + costTn*tn + costFp*fp + costFn*fn
accuracy_actual = (tp+tn)/(tp+tn+fp+fn)
precision_actual = tp/(tp+fp)
sensitivity_actual = tp/(tp+fn)
specificity_actual = tn/(tn+fp)

print(f'\nExpected Value || Your guess: {expected_value_guess} | Correct Answer: {expected_value_actual}')
print(f'Accuracy       || Your guess: {accuracy_guess} | Correct Answer: {accuracy_actual}')
print(f'Precision      || Your guess: {precision_guess} | Correct Answer: {precision_actual}')
print(f'Sensitivity    || Your guess: {sensitivity_guess} | Correct Answer: {sensitivity_actual}')
print(f'Specificity    || Your guess: {specificity_guess} | Correct Answer: {specificity_actual}')