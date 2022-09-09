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
    let n: i32 = input_t();
    let v: Vec<i32> = input_vec();

    let mut x = 0;
    for a in v {
        if a == x + 1 {
            x += 1;
        }
    }
    println!("{}", if x > 0 { n - x } else { -1 });
}
