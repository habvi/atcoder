use std::io::stdin;
use std::str::FromStr;

fn input_tuple<T: FromStr>() -> (T, T) {
    let mut s: String = String::new();
    stdin().read_line(&mut s).ok().unwrap();
    let mut itr = s.split_whitespace();
    (
        itr.next().unwrap().parse().ok().unwrap(),
        itr.next().unwrap().parse().ok().unwrap()
    )
}

fn gcd(a: usize, b: usize) -> usize {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn lcm(a: usize, b: usize) -> usize {
    a * b / gcd(a, b)
}

fn main() {
    let (a, b) = input_tuple();
    println!("{}", lcm(a, b));
}
