use std::io::stdin;
use std::str::FromStr;

fn input_t<T: FromStr>() -> T {
    let mut s: String = String::new();
    stdin().read_line(&mut s).ok().unwrap();
    s.trim().parse().ok().unwrap()
}

fn input_vec<T: FromStr>() -> Vec<T> {
    input_t::<String>()
        .split_whitespace()
        .map(|e| e.parse().ok().unwrap())
        .collect()
}

fn main() {
    let n: usize = input_t();
    let mut a: Vec<usize> = input_vec();

    let mut ans = 0;
    for i in 0..n - 1 {
        if a[i] > a[i + 1] {
            ans += a[i] - a[i + 1];
            a[i + 1] = a[i];
        }
    }
    println!("{}", ans);
}
