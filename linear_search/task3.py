def substitution_of_grades(estimates, max_estimate, min_estimate):
    for i in range(len(estimates)):
        if estimates[i] == min_estimate:
            estimates[i] = max_estimate
    return print(*estimates)



def main():
    estimates = list(map(int, input("Введите оценки разделяя пробелоа: ").split()))
    max_estimate = max(estimates)
    min_estimate = min(estimates)
    substitution_of_grades(estimates, max_estimate, min_estimate)



if __name__ == '__main__':
    main()