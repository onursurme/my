import itertools

# chapter6 soru c6_31'i çöz
# Suppose Bob has four cows that he wants to take across a bridge, but only
# one yoke, which can hold up to two cows, side by side, tied to the yoke.
# The yoke is too heavy for him to carry across the bridge, but he can tie
# (and untie) cows to it in no time at all. Of his four cows, Mazie can cross
# the bridge in 2 minutes, Daisy can cross it in 4 minutes, Crazy can cross
# it in 10 minutes, and Lazy can cross it in 20 minutes. Of course, when
# two cows are tied to the yoke, they must go at the speed of the slower cow.
# Describe how Bob can get all his cows across the bridge in 34 minutes.





















# bu çözüm hiç olmadı, zaten çözmüyor, çünkü her döngünün sonunda left ve right'ı döngünün başındaki hale geri getirmek lazım veya
# bir kopyasıyla çalışmak lazım
# önce şunu anlamak lazım : bu soru neden bu chapter'ın sonunda? bu chapter'daki bilgilerle nasıl bir ilişkisi var?

left = [2, 4, 10, 20]

for subset in itertools.combinations(left, 2):
    print(subset[0], ' ve ', subset[1], ' sağa geçiyor.')
    left = list(set(left)-set(subset))
    right = list(subset)
    print(left, right)
    total = max(subset[0], subset[1])
    print(subset[0], subset[1], ':', total)
    for subset2 in itertools.combinations(right, 1):
        print(subset2[0], ' sola geçiyor.')
        left = set(left).union(subset2)
        right = list(set(right)-set(subset2))
        print(left, right)
        total += subset2[0]
        print(subset2[0], ':', total)
        for subset3 in itertools.combinations(left, 2):
            print(subset3[0], ' ve ', subset3[1], ' sağa geçiyor.')
            right = set(right).union(subset3)
            left = list(set(left)-set(subset3))
            print(left, right)
            total += max(subset3[0], subset3[1])
            print(subset3[0], subset3[1], ':', total)
            for subset4 in itertools.combinations(right, 1):
                print(subset4[0], ' sola geçiyor.')
                left = set(left).union(subset4)
                right = list(set(right)-set(subset4))
                print(left, right)
                total += subset4[0]
                print(subset4[0], ':', total)
                for subset5 in itertools.combinations(left, 2):
                    print(subset5[0], ' ve ', subset5[1], ' sağa geçiyor.')
                    right = set(right).union(subset5)
                    left = list(set(left)-set(subset5))
                    print(left, right)
                    total += max(subset5[0], subset5[1])
                    print(subset5[0], subset5[1], ':', total)
                    input()
                    if total == 34 and len(left) == 0:
                        print("buldum")
                        input()
                    total = 0
                    left = [2, 4, 10, 20]
                    right = []
