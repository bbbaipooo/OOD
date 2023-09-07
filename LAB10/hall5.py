arr = input("Enter Input : ").split("/")
arr[0] = list(map(int,arr[0].split(" ")))
box_num=int(arr[1])

def put_to_box(start_idx,weight):
    cur_idx = start_idx
    while  weight - arr[0][cur_idx]>=0:
        weight -= arr[0][cur_idx]
        cur_idx +=1
        if cur_idx >= len(arr[0]):
            break
    return cur_idx
def is_Valid(weight):
    curidx =0

    for _ in range(box_num):
        cur_idx = put_to_box(cur_idx,weight)
        if cur_idx >= len(arr[0]):
            return True

    if cur_idx >= len(arr[0]):
        return False

w = max(max(arr[0]), sum(arr[0])//box_num)

while True:
    if is_Valid(w):
        break
    w+=1
print(f"Minimum weigth for {box_num} box(es) = {w}")