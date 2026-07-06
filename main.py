from finder import find_duplicates

print("=" * 50)
print("📂 Duplicate File Finder")
print("=" * 50)

folder = input("Enter folder path: ")

duplicates = find_duplicates(folder)

if not duplicates:
    print("\n✅ No duplicate files found.")
else:
    print("\n📋 Duplicate Files:")
    for original, duplicate in duplicates:
        print(f"\nOriginal : {original}")
        print(f"Duplicate: {duplicate}")
