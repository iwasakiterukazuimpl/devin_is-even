# devin_is-even

整数を受け取って偶数であるかを判定するPython関数です。

## 機能

`is_even(n)` 関数は整数を受け取り、偶数であれば `True`、奇数であれば `False` を返します。

## 使用方法

```python
from is_even import is_even

# 偶数の場合
print(is_even(4))  # True
print(is_even(0))  # True
print(is_even(-2)) # True

# 奇数の場合
print(is_even(3))  # False
print(is_even(1))  # False
print(is_even(-1)) # False
```

## テスト実行

pytestを使用してテストを実行できます：

```bash
pytest test_is_even.py
```

## 実装要件

- 入力 `n` は整数
- 偶数であれば `True`、奇数なら `False` を返す
- pytestでテストコードが書かれている
