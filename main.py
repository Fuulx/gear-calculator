def calculate_gear_ratio(driver_teeth, driven_teeth, input_rpm):
    if driver_teeth <= 0 or driven_teeth <= 0:
        raise ValueError("齿数必须大于 0")

    ratio = driven_teeth / driver_teeth
    output_rpm = input_rpm / ratio
    return ratio, output_rpm


print("=== 齿轮传动计算器 ===")

z1 = int(input("输入主动轮齿数："))
z2 = int(input("输入从动轮齿数："))
rpm = float(input("输入主动轮转速（rpm）："))

ratio, output_rpm = calculate_gear_ratio(z1, z2, rpm)

print(f"传动比：{ratio:.3f}")
print(f"从动轮转速：{output_rpm:.2f} rpm")
