type Props = {
  test: boolean;
  children: React.ReactElement;
};
const Maybe = ({ test, children }: Props) => <>{test && children}</>;

export default Maybe;
