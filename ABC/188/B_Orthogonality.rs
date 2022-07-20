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
    let va: Vec<i64> = input_vec();
    let vb: Vec<i64> = input_vec();

    let mut total: i64 = 0;
    for i in 0..n {
        total += va[i] * vb[i];
    }
    println!("{}", if total == 0 { "Yes" } else { "No" });
}