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
    #[allow(unused_variables)]
    let n: usize = input_t();
    let v: Vec<usize> = input_vec();

    let num: Vec<usize> = vec![0, 1, 0, 1, 2, 3, 0, 1, 0];
    let mut ans: usize = 0;
    for x in v {
        ans += num[x - 1];
    }
    println!("{}", ans);
}