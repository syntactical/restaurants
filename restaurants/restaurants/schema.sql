drop table if exists restaurants;

create table restaurants (
  id integer primary key autoincrement,
  name text not null,
  address text not null,
  zip_code text not null,
  city text not null,
  phone text not null,
  grade text not null
);
