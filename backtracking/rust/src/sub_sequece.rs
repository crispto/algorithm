fn sub_sequence<T: std::fmt::Debug + Clone>(v: Vec<T>) {
    let mut tmp: Vec<T> = Vec::new();
    sub_sequence_help(0, &mut tmp, &v);
}

fn sub_sequence_help<T: std::fmt::Debug + Clone>(index: i32, tmp: &mut Vec<T>, v: &Vec<T>) {
    if v.len() as i32 == index {
        print!("{:?}\n", *tmp);
        return;
    }
    sub_sequence_help(index + 1, tmp, &v);
    tmp.push(v[index as usize].clone());
    sub_sequence_help(index + 1, tmp, &v);
    tmp.pop();
}

pub fn sub_sequence_main() {
    let v1: Vec<i32> = vec![1, 2, 3, 4];
    let v2: Vec<&str> = vec!["A", "B", "C"];
    sub_sequence(v1);
    sub_sequence(v2);
}
