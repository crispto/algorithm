mod base64_ciphers;
fn main() {
    let v = "abcd";
    let en = base64_ciphers::encode(&v);
    println!("{}", en);

    let de = base64_ciphers::decode(&en).unwrap();
    println!("{}", de);
}
