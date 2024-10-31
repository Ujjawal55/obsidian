"""
problem statement is to find the minimum cost of matrix multiplication

"""


def mcm(arr, i, j):

    # base case
    """
    this smallest possible valid input is i == j, in the cose will be 0
    this largest possible invalid input is i > j. it does not make sense
    """
    if i >= j:
        return 0

    """
        the idea is to break [i, k] and [k+1, j]
        the value of k should start from i because in that we can get the first matrix dimension  following above split method.
        and if it end before j then it is possible to have k + 1 ( on case k == j - 1 and k + 1 == j)
    """
    min_cost = float("inf")

    for k in range(i, j):
        temp_cost = mcm(arr, i, k) + mcm(arr, k + 1, j) + (arr[i - 1] * arr[k] * arr[j])

        if temp_cost < min_cost:
            min_cost = temp_cost

    """
    1. note we donot have to worry about this return statement each sub-branch will start with the min_cost = inf then, at the end of
    2. calcuation will return a positive value, this value will be returned to the function who called that sub-branch
    3. then again the branch call the above function will also have the min_cost = -inf then, again it get a value and will returned to the function
       who call it
    4. finally when we reached the end of the function min_cost value will be returned to the main_function call.......

    """
    return min_cost


def main():
    arr = [40, 20, 30, 10, 30]
    min_cost = float("inf")
    min_cost = mcm(
        arr, 1, len(arr) - 1
    )  # starting the i value with 1 because then it is possible to get the dimension of the first matrix. arr[i-1] x arr[i]
    print(f"The minimum cost is: {min_cost}")


if __name__ == "__main__":
    main()
