extra_space = int(input("Enter extra space: "))
sanitizers_count = int(input("Enter number of hand sanitizer: "))
wipes_count = int(input("Enter number of wipes: "))

sanitizers_needed = extra_space // 5
wipes_needed = extra_space % 5

total = 0
if sanitizers_count >= sanitizers_needed:
    total = sanitizers_needed * 5
else:
    total = sanitizers_count * 5
    wipes_needed += (sanitizers_needed - sanitizers_count) * 5

total += wipes_needed if wipes_count >= wipes_needed else 0

print((
        f"{wipes_needed} package of wipes" if total == extra_space
        else "Cannot fill extra space exactly."
))
