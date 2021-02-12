unit uIsogram;

interface

uses
  System.SysUtils;

function isIsogram(aValue: string): boolean;

implementation

uses
  System.RegularExpressions;

function isIsogram(aValue: string): boolean;
var
  character: string;
  numerCorrepondencia: integer;
  entradaFormatada: string;
begin
  entradaFormatada := TRegEx.Replace(aValue.ToLower, '-| ', '');
  for character in entradaFormatada do
  begin
    numerCorrepondencia := TRegEx.Matches(entradaFormatada, character).Count;
    if (numerCorrepondencia > 1) then
    begin
      Exit(false);
    end;
  end;
  Exit(true);
end;

end.
