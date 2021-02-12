unit utwofer;

interface

  function twoFer(value: string = 'you'): string;

implementation

function twoFer(value: string = 'you'): string;
begin
  Result := 'One for ' + value + ', one for me.';
end;

end.
