# cook your dish here
def is_scalene_triangle(a, b, c):
    return a != b and b != c and a != c

def main():
    # Input the number of test cases
    T = int(input())

    for _ in range(T):
        # Input the sides of the triangle
        a, b, c = map(int, input().split())

        # Check if the triangle is scalene
        if is_scalene_triangle(a, b, c):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
