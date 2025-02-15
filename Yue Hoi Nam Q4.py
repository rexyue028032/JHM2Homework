def main():
    heights = []
    
    while len(heights) < 4:
        try:
            height = float(input(f"please enter the {len(heights) + 1} height of the student (0-200 cm):"))
            
            if height < 0:
                print("Height must be positive.")
            elif height > 200:
                print("Height is greater than 200cm.")
            else:
                heights.append(height)
        except ValueError:
            print("please enter a valid number.")

    print("End of input.")
    
    average_height = sum(heights) / len(heights)
    max_height = max(heights)

    print(f"Average height of classmates: {average_height:.2f} cm")
    print(f"The highest height of classmates: {max_height:.2f} cm")

if __name__ == "__main__":
    main()