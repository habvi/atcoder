use std::io::stdin;
use std::str::FromStr;
use itertools::izip;
use std::cmp::Reverse;

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
    let n: u32 = input_t();
    let v: Vec<usize> = input_vec();

    let mut a: Vec<_> = izip!(v, 1..).collect::<Vec<_>>();
    let mid: usize = 2_usize.pow(n) / 2;
    a[..mid].sort_by_key(|&(x, _)| Reverse(x));
    a[mid..].sort();

    let (s1, p1): (usize, usize) = a[0];
    let (s2, p2): (usize, usize) = a[mid * 2 - 1];
    println!("{}", if s1 > s2 { p2 } else { p1 });
}